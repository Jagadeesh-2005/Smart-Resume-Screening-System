from flask import Flask, render_template, request
import sqlite3
import os

from utils.resume_parser import extract_text_from_pdf
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity
from utils.scorer import (
    calculate_final_score,
    get_recommendation
)

from data.job_descriptions import JOB_DESCRIPTIONS

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    if "resume" not in request.files:
        return "No resume uploaded"

    resumes = request.files.getlist("resume")

    if len(resumes) == 0:
        return "Please upload at least one resume"

    job_role = request.form["job_role"]

    if job_role not in JOB_DESCRIPTIONS:
        return "Invalid Job Role Selected"

    job_description = JOB_DESCRIPTIONS[job_role]
    jd_skills = extract_skills(job_description)

    rankings = []

    for resume in resumes:

        if resume.filename == "":
            continue

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            resume.filename
        )

        resume.save(file_path)

        resume_text = extract_text_from_pdf(file_path)

        resume_skills = extract_skills(resume_text)

        matched_skills = list(
            set(resume_skills).intersection(set(jd_skills))
        )

        missing_skills = list(
            set(jd_skills) - set(resume_skills)
        )

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        if len(jd_skills) > 0:
            skill_match_score = (
                len(matched_skills) / len(jd_skills)
            ) * 100
        else:
            skill_match_score = 0

        final_score = calculate_final_score(
            similarity_score,
            skill_match_score
        )

        recommendation = get_recommendation(
            final_score
        )

        rankings.append({
            "name": resume.filename,
            "similarity": round(similarity_score, 2),
            "skill_score": round(skill_match_score, 2),
            "final_score": round(final_score, 2),
            "recommendation": recommendation,
            "matched": matched_skills,
            "missing": missing_skills
        })

        try:
            conn = sqlite3.connect(
                "database/candidates.db"
            )

            cursor = conn.cursor()

            cursor.execute(
                """
                INSERT INTO candidates
                (name, score, recommendation)
                VALUES (?, ?, ?)
                """,
                (
                    resume.filename,
                    final_score,
                    recommendation
                )
            )

            conn.commit()
            conn.close()

        except Exception as e:
            print("Database Error:", e)

    if not rankings:
        return "No valid resumes uploaded"

    rankings.sort(
        key=lambda x: x["final_score"],
        reverse=True
    )

    best_candidate = rankings[0]

    return render_template(
        "result.html",
        job_role=job_role,
        rankings=rankings,
        similarity=best_candidate["similarity"],
        skill_score=best_candidate["skill_score"],
        final_score=best_candidate["final_score"],
        recommendation=best_candidate["recommendation"],
        matched=best_candidate["matched"],
        missing=best_candidate["missing"]
    )


if __name__ == "__main__":
    app.run(debug=True)
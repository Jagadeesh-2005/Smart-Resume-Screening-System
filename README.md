# Smart Resume Screening System

## Overview

The Smart Resume Screening System is a Machine Learning-based web application developed to automate the resume screening process. The system compares uploaded resumes with a selected job description, calculates an ATS (Applicant Tracking System) score, identifies matched and missing skills, and ranks candidates based on their suitability for the selected role.

This application helps recruiters save time, reduce manual effort, and shortlist the most relevant candidates efficiently.

---

# Features

* Upload single or multiple PDF resumes
* Select a job role from predefined job descriptions
* Extract text from PDF resumes
* Identify technical skills from resumes
* Compare resumes with job descriptions
* Calculate similarity using TF-IDF and Cosine Similarity
* Calculate ATS (Applicant Tracking System) scores
* Display matched and missing skills
* Rank multiple candidates automatically
* Store candidate information in an SQLite database
* User-friendly web interface built with Flask

---

# Technologies Used

## Frontend

* HTML5
* CSS3

## Backend

* Python
* Flask

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Cosine Similarity

## Database

* SQLite

## Python Libraries

* Flask
* pdfplumber
* scikit-learn
* sqlite3
* os

---

# Project Structure

```text
Smart-Resume-Screening-System/
│
├── app.py
├── requirements.txt
│
├── data/
│   └── job_descriptions.py
│
├── database/
│   └── candidates.db
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── uploads/
│
└── utils/
    ├── resume_parser.py
    ├── skill_extractor.py
    ├── similarity.py
    └── scorer.py
```

---

# Project Workflow

1. The user opens the application.
2. One or more PDF resumes are uploaded.
3. A job role is selected.
4. The application saves the uploaded resumes.
5. Text is extracted from each PDF using **pdfplumber**.
6. Skills are extracted from the resume text.
7. Skills are extracted from the selected job description.
8. Resume text is compared with the job description using **TF-IDF** and **Cosine Similarity**.
9. A similarity score is calculated.
10. A skill match score is calculated.
11. The final ATS score is generated.
12. Candidates are ranked according to their ATS scores.
13. Results are displayed on the dashboard.
14. Candidate information is stored in the SQLite database.

---

# Machine Learning Approach

This project uses Natural Language Processing (NLP) techniques to compare resumes with job descriptions.

### TF-IDF Vectorization

TF-IDF (Term Frequency – Inverse Document Frequency) converts textual data into numerical vectors by assigning higher importance to meaningful words.

### Cosine Similarity

Cosine Similarity measures how closely the resume matches the selected job description. The result is expressed as a percentage.

### ATS Score Formula

```
Final ATS Score =
(0.6 × Similarity Score)
+
(0.4 × Skill Match Score)
```

---

# Recommendation Criteria

| ATS Score     | Recommendation       |
| ------------- | -------------------- |
| 85% and above | Strongly Recommended |
| 70% – 84%     | Recommended          |
| 50% – 69%     | Consider             |
| Below 50%     | Rejected             |

---

# Installation Guide

## Step 1: Clone the Repository

```bash
git clone https://github.com/Jagadeesh-2005/Smart-Resume-Screening-System.git
```

## Step 2: Navigate to the Project Folder

```bash
cd Smart-Resume-Screening-System
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Run the Application

```bash
python app.py
```

## Step 5: Open the Application

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# Advantages

* Reduces manual resume screening effort.
* Speeds up candidate shortlisting.
* Provides consistent candidate evaluation.
* Supports multiple resume uploads.
* Displays detailed skill analysis.
* Easy to use and lightweight.

---

# Limitations

* Supports PDF resumes only.
* Uses predefined technical skills.
* Accuracy depends on the quality of the resume and job description.
* Does not process images or graphics inside resumes.

---

# Future Enhancements

* AI-based resume improvement suggestions
* AI-generated interview questions
* Internship and job recommendations
* Resume ranking analytics
* Export reports to Excel or PDF
* Email notifications for shortlisted candidates
* Advanced NLP-based skill extraction
* Recruiter dashboard with analytics

---

# Author

**Jagadeesh**

GitHub: https://github.com/Jagadeesh-2005

---

# License

This project is developed for educational and learning purposes. Feel free to use and modify it for academic or personal projects.

---

## Acknowledgements

* Flask Documentation
* Scikit-learn Documentation
* pdfplumber Documentation
* SQLite Documentation

---

## Contributing

Contributions, suggestions, and improvements are welcome. Feel free to fork the repository, create a feature branch, and submit a pull request.

---

## Contact

If you have any questions or suggestions, you can reach out through my GitHub profile:

**https://github.com/Jagadeesh-2005**


````markdown
<div align="center">

# 📄 Smart Resume Screening System

### 🚀 AI-Powered Resume Analysis & ATS Candidate Ranking

Automatically analyze resumes, compare them with job descriptions, calculate ATS scores, and rank candidates using Machine Learning.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-Web_App-000000?style=for-the-badge&logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite)

</div>

---

## ✨ Features

- 📄 Upload one or multiple PDF resumes
- 🎯 Select a job role for analysis
- 🤖 Automatic resume text extraction
- 🧠 Skill extraction from resumes
- 📊 ATS score calculation
- 🔍 Resume similarity using TF-IDF & Cosine Similarity
- ✅ Matched and missing skills analysis
- 🏆 Candidate ranking dashboard
- 💾 SQLite database integration
- 🌐 Responsive Flask web application

---

## 🛠️ Tech Stack

| Category | Technologies |
|----------|--------------|
| Frontend | HTML, CSS |
| Backend | Python, Flask |
| Machine Learning | Scikit-learn |
| NLP | TF-IDF Vectorizer, Cosine Similarity |
| Database | SQLite |
| PDF Processing | pdfplumber |

---

## 📂 Project Structure

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

## ⚙️ Workflow

```text
Upload Resume(s)
        │
        ▼
Extract PDF Text
        │
        ▼
Extract Skills
        │
        ▼
Select Job Description
        │
        ▼
Calculate Similarity
(TF-IDF + Cosine Similarity)
        │
        ▼
Calculate Skill Match
        │
        ▼
Generate ATS Score
        │
        ▼
Rank Candidates
        │
        ▼
Display Dashboard
```

---

## 📊 ATS Score Formula

```text
Final ATS Score =
(0.6 × Similarity Score)
+
(0.4 × Skill Match Score)
```

---

## 🏅 Recommendation Levels

| ATS Score | Recommendation |
|-----------|----------------|
| ⭐ 85%+ | Strongly Recommended |
| ✅ 70%–84% | Recommended |
| ⚠️ 50%–69% | Consider |
| ❌ Below 50% | Rejected |

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Jagadeesh-2005/Smart-Resume-Screening-System.git
```

### 2️⃣ Open the project

```bash
cd Smart-Resume-Screening-System
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application

```bash
python app.py
```

### 5️⃣ Open in your browser

```
http://127.0.0.1:5000
```

---

## 📸 Preview

> Add screenshots of your application here.

| Home Page | Dashboard |
|-----------|-----------|
| *(Add Screenshot)* | *(Add Screenshot)* |

---

## 🔮 Future Improvements

- 🤖 AI-powered resume feedback
- 💬 Interview question generation
- 📧 Email notifications
- 📈 Analytics dashboard
- 📄 Export reports to Excel/PDF
- 💼 Internship & job recommendations

---

## 👨‍💻 Author

**Jagadeesh**

- GitHub: https://github.com/Jagadeesh-2005

---

<div align="center">

### ⭐ If you found this project useful, consider giving it a star!

Made with ❤️ using Python, Flask, and Machine Learning.

</div>
````

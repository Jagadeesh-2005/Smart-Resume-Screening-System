````markdown
# 📄 Smart Resume Screening System Using Machine Learning

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange?style=for-the-badge)
![SQLite](https://img.shields.io/badge/Database-SQLite-blue?style=for-the-badge&logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

### 🚀 AI-Powered Resume Screening & ATS Candidate Ranking System

Automatically analyze resumes, compare them with job descriptions, calculate ATS scores, and rank candidates using Machine Learning.

</div>

---

## 📌 Overview

The **Smart Resume Screening System** is a Machine Learning-powered web application that automates the resume screening process.

Instead of manually reviewing resumes, the system:

- Extracts text from PDF resumes
- Identifies technical skills
- Compares resumes with job descriptions
- Calculates ATS scores
- Ranks candidates automatically
- Displays matched and missing skills

This project helps recruiters shortlist candidates quickly and efficiently.

---

# ✨ Features

- 📄 Upload Single or Multiple PDF Resumes
- 🤖 Automatic Resume Analysis
- 🎯 ATS Score Calculation
- 📊 Candidate Ranking
- ✅ Matched Skills Detection
- ❌ Missing Skills Detection
- 📈 Resume Similarity Analysis
- 💾 SQLite Database Integration
- 🌐 Beautiful Flask Web Dashboard
- 📱 Responsive User Interface

---

# 🛠 Tech Stack

### Frontend

- HTML5
- CSS3

### Backend

- Python
- Flask

### Machine Learning

- Scikit-Learn
- TF-IDF Vectorizer
- Cosine Similarity

### Database

- SQLite

### Libraries

- pdfplumber
- scikit-learn
- Flask

---

# 📂 Project Structure

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

# ⚙️ Workflow

```text
Upload Resume(s)
        │
        ▼
PDF Text Extraction
        │
        ▼
Skill Extraction
        │
        ▼
Job Description Selection
        │
        ▼
Resume Similarity (TF-IDF + Cosine Similarity)
        │
        ▼
Skill Match Calculation
        │
        ▼
ATS Score Generation
        │
        ▼
Candidate Ranking
        │
        ▼
Dashboard Display
```

---

# 🧠 Machine Learning Approach

This project uses Natural Language Processing (NLP) techniques.

### TF-IDF Vectorization

Converts resume text and job description into numerical vectors by assigning importance to words.

### Cosine Similarity

Measures the similarity between the resume and the selected job description.

### ATS Score Formula

```
Final ATS Score =
(0.6 × Similarity Score)
+
(0.4 × Skill Match Score)
```

---

# 📊 Recommendation Criteria

| ATS Score | Recommendation |
|-----------|----------------|
| 85% and above | ⭐ Strongly Recommended |
| 70% – 84% | ✅ Recommended |
| 50% – 69% | ⚠️ Consider |
| Below 50% | ❌ Rejected |

---

# 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/Jagadeesh-2005/Smart-Resume-Screening-System.git
```

### Navigate to the Project

```bash
cd Smart-Resume-Screening-System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# 📸 Screenshots

> Add screenshots of your application here.

Example:

```
screenshots/
├── home.png
├── dashboard.png
└── ranking.png
```

---

# 🎯 Future Enhancements

- AI-powered Resume Suggestions
- Interview Question Generation
- Resume Ranking Analytics
- Internship Recommendations
- Excel/PDF Report Export
- Email Notifications
- Admin Dashboard
- Advanced NLP-based Skill Extraction

---

# 👨‍💻 Author

**Jagadeesh**

GitHub: https://github.com/Jagadeesh-2005

---

# ⭐ Support

If you found this project helpful:

- ⭐ Star this repository
- 🍴 Fork the project
- 💡 Share your feedback

---

<div align="center">

### Thank you for visiting this repository! 🚀

</div>
````

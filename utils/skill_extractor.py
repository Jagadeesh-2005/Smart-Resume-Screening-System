def extract_skills(text):

    skills_db = [
    "python", "java", "c++", "sql", "mysql", "mongodb",
    "machine learning", "deep learning", "tensorflow",
    "pytorch", "nlp", "computer vision", "generative ai",
    "langchain", "llm", "pandas", "numpy", "statistics",
    "power bi", "tableau", "excel", "data analysis",
    "data visualization", "html", "css", "javascript",
    "react", "bootstrap", "tailwind css", "flask",
    "django", "fastapi", "node.js", "rest api",
    "git", "docker", "kubernetes", "jenkins",
    "aws", "azure", "google cloud platform",
    "terraform", "linux", "network security",
    "ethical hacking", "penetration testing",
    "siem", "incident response", "redis",
    "dbms", "operating systems",
    "data structures", "algorithms",
    "system design", "cloud security"
]

    found_skills = []

    text = text.lower()

    for skill in skills_db:

        if skill in text:
            found_skills.append(skill)

    return found_skills
from faker import Faker
import json
import random

fake = Faker()
skills_list = [
    "Python", "Java", "C++", "JavaScript", "HTML", "CSS", "SQL",
    "Django", "Flask", "React", "Angular", "Node.js",
    "Docker", "Kubernetes", "AWS", "GCP", "Azure",
    "Machine Learning", "Data Analysis", "Pandas", "NumPy",
    "Git", "CI/CD", "REST APIs"
]

resumes = []
for _ in range(10):
    a,b = float("inf"),float("-inf")
    while a>b:
        a = random.randint(0,len(skills_list))
        b = random.randint(0,len(skills_list))
    have_skills = skills_list[a:b]
    candidate = {"name": fake.name(), "email": fake.email(), "content": f"Have knowledge of {', '.join(have_skills)}."}
    resumes.append(candidate)

with open("resumes.json", "w") as f:
    json.dump(resumes, f, indent=4)
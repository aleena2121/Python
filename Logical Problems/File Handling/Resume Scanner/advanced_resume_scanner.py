import json
import re 

with open("resumes.json", "r") as f1:
    data = json.load(f1)
    matched_candidates = []
    required_keywords = ["Python","Docker"]
    for candidate in data:
        isValidEmail = re.search(r"[\w]+@[\w]{1,}\.[\w]{2,}",candidate['email'])
        if isValidEmail == None:
            print(f'Invalid Email for {candidate["email"]}')
        matched_skill = []
        for skill in required_keywords:
            if skill.lower() in candidate["content"].lower():
                matched_skill.append(skill)
        if len(matched_skill) > 0:
            matched_candidates.append({"name": candidate["name"], "email": candidate["email"], "matched_keyword": matched_skill})
        

with open("shortlisted.json","w") as f2:
        json.dump(matched_candidates, f2,indent=4)
              
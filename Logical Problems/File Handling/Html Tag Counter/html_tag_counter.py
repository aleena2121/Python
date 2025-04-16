import json 
import re 
from collections import Counter

with open("page.html","r") as f1:
    content = f1.read()

tags = re.findall(r"<\s*\w+>",content)
tag_count = Counter(tags)

with open("tag_count.json","w") as f2:
    json.dump(tag_count,f2,indent=4)

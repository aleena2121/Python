import json 
import re 

logs = {}
with open("system_log.txt","r") as f1:
    entries = f1.readlines()
    for entry in entries:
        email = re.search(r"[\w\.-_]+@[\w]{1,}\.[\w]{2,}", entry)
        log_level = re.search(r"[A-Z]+:", entry).group(0)[:-1]
        ip_address = re.search(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", entry)
        
        ip_address = ip_address.group(0) if ip_address != None else None
        if email == None and "admin" in entry:
            email = "admin"
        else: 
            email = email.group(0)
        
        if email in logs:
            logs[email]["count"] += 1
            logs[email]["ips"].append(ip_address)
        else:
            logs[email] = {"count" : 1, "ips": [ip_address]}

with open("log_summary.json","w") as f2:
    json.dump(logs, f2, indent=4)
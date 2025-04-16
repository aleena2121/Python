import json 
import re 

with open("chat.txt","r") as f1, open("chat.json","w") as f2:
    chats = f1.readlines()
    logs = []
    for chat in chats:
        log = {}
        time = re.search(r"\d{2}:\d{2}", chat)
        sender = re.search(r"] [A-Za-z]+", chat)
        receiver = re.search(r"->\s[A-Za-z]+", chat)
        message = re.search(r":\s.*", chat)


        log["time"] = time.group(0)
        log["sender"] = sender.group(0)[2:]
        log["message"] = message.group(0)[2:]
        if receiver!=None:
            log["reply_to"] = receiver.group(0)[3:]
        else:
            log["reply_to"] = None
        logs.append(log)

    json.dump(logs, f2, indent=4)
from faker import Faker
import random

fake = Faker()

with open("chat.txt", "w") as f:
    senders_name = fake.first_name()
    receivers_name = fake.first_name()
    for _ in range(100):
        senders_name, receivers_name = receivers_name, senders_name
        time = fake.date_time()
        time = time.strftime("%H:%M")
        sentence = fake.sentence()
        type = random.choice(["reply", "not-reply"])
        match type:
            case "not-reply":
                log = f"[{time}] {senders_name}: {sentence}"
            case "reply":
                log = f"[{time}] {senders_name} -> {receivers_name}: {sentence}"
        
        f.write(log + "\n")
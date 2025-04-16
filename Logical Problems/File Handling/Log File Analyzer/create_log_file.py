from faker import Faker
import random

fake = Faker()
with open("system_log.txt","w") as f:
    for _ in range(1000):
        email = fake.email()
        status = random.choice(["logged-in","failed-login","exceeded_attempts"])
        match status:
            case "logged-in":
                sentence = f"User {email} logged in from {fake.ipv4()}."
            case "failed-login":
                sentence = f"Failed login for user {email} from IP {fake.ipv4()}."
            case "exceeded_attempts":
                sentence =  f"User {email} exceeded login attempts"

        log = f"[{fake.date()} {fake.time()}] {random.choice(['INFO', 'ERROR', 'WARNING'])}: {sentence}"
        f.write(log + "\n") 
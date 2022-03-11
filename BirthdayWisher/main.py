import smtplib
import json

try:
    with open("sender_email_creds.json") as file:
        sender = json.load(file)
        email = sender["email"]
        password = sender["password"]
except FileNotFoundError:
    # Exit the program.
    print("Sender credentials file not found")
    exit()

message = "Hello!"
recipient_email_address = "foo.bar@gmail.com"

HOST = "smtp.gmail.com"
connection = smtplib.SMTP(HOST)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=recipient_email_address, msg=message)
connection.close()

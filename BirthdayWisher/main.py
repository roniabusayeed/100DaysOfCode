import random
import glob
import os
import pandas
import datetime as dt
import json
import smtplib


def gmail(sender_email, sender_password, recipient_email, msg):
    """Sends an email using gmail smtp"""
    host = "smtp.gmail.com"
    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(sender_email, sender_password)
        connection.sendmail(sender_email, recipient_email, msg)


# Read birthday email templates.
templates = []
# Iterate over all template files in templates directory.
for template_filename in glob.glob(os.path.join("templates", "template*.txt")):
    # Read the content of each template file and add it to the list of templates.
    with open(template_filename) as template_file:
        templates.append(template_file.read())


def create_message(sender_name, recipient_name):
    """Picks a random message from templates and replaces placeholders with given names
    and returns the new string"""
    template = random.choice(templates)
    template = template.replace("[sender]", sender_name)
    return template.replace("[recipient]", recipient_name)


# Load sender's credentials.
with open("sender_email_creds.json", "r") as sender_file:
    sender = json.load(sender_file)

# If anyone has their birthday today, email them.
birthdays_data = pandas.read_csv("contacts.csv")
birthdays = birthdays_data.to_dict(orient="records")
today = dt.datetime.now()
for birthday in birthdays:
    if birthday['month'] == today.month and birthday['day'] == today.day:
        message = create_message(sender['name'], birthday['name'])
        gmail(sender['email'], sender['password'], birthday['email'], message)
        print(f"Email sent to {birthday['name']}")

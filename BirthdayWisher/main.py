"""
Sends a birthday email to everyone who has their birthday today.
Steps:
1. Read a list of birthdays [(name, email, date of birth),...]
2. For each of the dates, check if it's today's date.
3. If it is today's date, "email them".

Sending an email steps:
1. create message.
steps:
    1. pick a random birthday email template.
    2. replace the placeholders with their name.
2. send email:
steps:
    1. create email connection.
    2. activate tls.
    3. login.
    4. send email.
"""

import random
import glob
import os

# Pick a random birthday email template.
templates = []
# Iterate over all template files in templates directory.
for template_filename in glob.glob(os.path.join("templates", "template*.txt")):
    # Read the content of each template file and add it to the list of templates.
    with open(template_filename) as template_file:
        templates.append(template_file.read())
# Pick one of the templates randomly.
random_template = random.choice(templates)

import datetime as dt
import pandas
import random
import smtplib


email = "romsontesting@gmail.com"
password = "Welcome2021*"
to_addr = "info@vbel.nl"

now = dt.datetime.now()
today = (now.month, now.day)

# Add names to birthdays.csv
# with open("birthdays.csv", "a") as file:
#     file.write("Name, name@gmail.com, 2002, 01, 01\n")

data_csv = pandas.read_csv("birthdays.csv")
birthdays = {(data.month, data.day): data for (index, data) in data_csv.iterrows()}

if today in birthdays:
    person = birthdays[today]

    with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as source_letter:
        source_contents = source_letter.read()
        letter_to_send = source_contents.replace("[NAME]", person["name"])
        mssg = f"Subject: Happy Birhtday!\n\n{letter_to_send}"

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email, password=password)
        connection.sendmail(
            from_addr="Birthday service",
            to_addrs=to_addr,
            msg=mssg
        )

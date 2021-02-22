import datetime as dt
import pandas
import random
import smtplib


email = "***"
password = "***"
to_addr = "***"

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
today = f"{day}-{month}-{year}"

# Add names to birthdays.csv
# with open("birthdays.csv", "a") as file:
#     file.write("Romero, romsontesting@gmail.com, 1982, 12, 09\n")

# Create DataFrame
data = pandas.read_csv("birthdays.csv")

# Open letter templates
with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", mode="r") as source_letter:
    source_contents = source_letter.read()

    # Check for date, name etc..
    for (index, person) in data.iterrows():
        if f"{person['day']}-{person['month']}-{person['year']}" == "9-12-1982":
            name = person['name']
            print(name)
            # Replace name
            letter_to_send = source_contents.replace("[NAME]", name)
            mssg = f"Subject: Happy Birhtday!\n\n{letter_to_send}"

            # Send email
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(
                    from_addr="Birthday service",
                    to_addrs=to_addr,
                    msg=mssg
                )

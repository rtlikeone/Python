import smtplib
from timeclass import Time
import random

FROM_ADDR = "*****"
TO_ADDR = "*****"
EMAIL = "*****"
PASSWORD = "*****"

time = Time()

with open("quotes.txt", mode="r") as quotes:
    data = quotes.read().splitlines()
    msg = f"Subject:Master, your daily quote\n\n{random.choice(data)}"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=EMAIL, password=PASSWORD)
    if time.day != 6:
        connection.sendmail(
            from_addr=FROM_ADDR,
            to_addrs=TO_ADDR,
            msg=msg
        )

print(time.day)
print(random.choice(data))

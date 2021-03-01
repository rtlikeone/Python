import requests
import datetime as dt
import smtplib
import time

MY_LAT = 51.9286684
MY_LNG = 4.4928477
MY_EMAIL = "email"
PASSWORD = "password"

# Get ISS data.
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
iss_response.raise_for_status()
iss_data = iss_response.json()
iss_lat = float(iss_data["iss_position"]["longitude"])
iss_lng = float(iss_data["iss_position"]["latitude"])


def is_iss_overhead():
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True


def is_night():
    # https://sunrise-sunset.org/api (parameters)
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0
    }
    sunset_api = "https://api.sunrise-sunset.org/json"
    senset_response = requests.get(url=sunset_api, params=parameters, )
    senset_response.raise_for_status()
    senset_data = senset_response.json()

    # Get 24hr clock by splitting the time string.
    sunrise = int(senset_data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(senset_data["results"]["sunset"].split("T")[1].split(":")[0])

    # Compare time.
    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="email@gmail.com",
                msg=f"Subject: Master, ISS is near!\n\nMaster, Look up, ISS is near!\n"
                    f"Current lat: {iss_lat}, lng: {iss_lng}\n"
                    f"https://www.google.com/maps/search/?api=1&query={iss_lat},{iss_lng}\n"
                    f"Check it out!"
            )

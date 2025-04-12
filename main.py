import requests
from datetime import  datetime
import smtplib
import time

my_mail = "demo@gmail.com"
password = "jbje zuwo iprp mbvi"

MY_LAT = 26.227430
MY_LONG = 84.365417

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # my position is within +5 or -5 degrees of the ISS position
    if MY_LONG -5 <= iss_longitude <= MY_LONG +5 and MY_LAT-5 <= iss_latitude <= MY_LAT+5:
        return  True


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response1 = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response1.raise_for_status()
    data1 = response1.json()

    sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return  True

while True:
    print("hii")
    time.sleep(60)
    if is_dark() and is_iss_overhead():
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_mail , password=password )
            for _ in range(1, 3):
                connection.sendmail(from_addr= my_mail,
                                    to_addrs= my_mail,
                                    msg="Subject:ISS Space Station\n\nLook into the sky!"
                                    )

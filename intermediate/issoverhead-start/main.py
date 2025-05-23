import requests
from datetime import datetime
import smtplib

MY_LAT = 12.902369 
MY_LONG = 77.562295 

email = "anirudhmulky@gmail.com"
password = "****************"

def is_overhead():

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <=MY_LONG+5:
        return True
        
def is_visible():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <=sunrise:
        return True
    

def send_mail():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(email,password)
    connection.sendmail(from_addr=email,to_addrs="anirudhmulky108@gmail.com",msg="Subject:ISS Overhead!\n\nWatch out! The International space station is overhead.")


if is_overhead and is_visible:
    send_mail()




import bs4
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

email = "anirudhmulky@gmail.com"
password = "nwcxmdexmhrjysse"

response = requests.get(url="https://appbrewery.github.io/instant_pot/")

webpage = response.text

soup = bs4.BeautifulSoup(webpage,"html.parser")

price_span = soup.find(name="span", class_="aok-offscreen")

price = price_span.getText()

price_without_currency = price.split("$")[1]

price_float = float(price_without_currency)

broken_title = soup.find(id="productTitle").getText().strip()

title = " ".join(broken_title)

if price_float < 100:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(os.environ["EMAIL"],os.environ["PASSWORD"])
    connection.sendmail(from_addr=os.environ["EMAIL"],to_addrs=os.environ["EMAIL"],msg=f"Subject:Amazon price alert!\n\n{title} is for {price}.".encode("utf-8"))

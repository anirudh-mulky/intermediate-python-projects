# import smtplib

# my_email = "anirudhmulky@gmail.com"


# connection = smtplib.SMTP("smtp.gmail.com")
# connection.starttls()    #for encryption
# connection.login(user=my_email,password=password)
# connection.sendmail(from_addr=my_email, to_addrs="anirudhmulky108@gmail.com",msg="Subject:hello bro\n\nThis is the body of my email")
# connection.close()
import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()

email = "anirudhmulky@gmail.com"
password = "************8"

if weekday == 0:
    with open("quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=email,password=password)
    connection.sendmail(from_addr=email,to_addrs="xyz@gmail.com", msg=f"Subject:Motivation\n\n{quote}")
    connection.close()


date_of_birth = dt.datetime(year=2006,month=5,day=7)

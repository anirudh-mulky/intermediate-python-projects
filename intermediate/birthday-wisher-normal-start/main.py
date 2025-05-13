import datetime as dt
import random
import pandas
import smtplib

email = "anirudhmulky@gmail.com"
password = "*************"


today = (dt.datetime.now().month,dt.datetime.now().day)


data = pandas.read_csv("birthdays.csv")


new_dict = {(data_row.month,data_row.day): data_row for (index, data_row) in data.iterrows()}

if (today) in new_dict:
    person = new_dict[today]
    file_path = f"/Users/anirudhmulky/Desktop/python/birthday-wisher-normal-start/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", person["name"])


    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(email,password=password)
    connection.sendmail(from_addr=email,to_addrs=person["email"],
                        msg=f"Subject:Happy Birthday!\n\n{contents}")
# 4. Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.




import smtplib
import datetime as dt
import random
import pandas

now = dt.datetime.now()
month = now.month
day = now.day

today = (month, day)
data = pandas.read_csv("list_file.csv")
new_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in new_dict:
    birthday_person = new_dict[today]
    file_path =f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents= contents.replace("[NAME]", birthday_person["name"])

# [NAME] is what will be replaced in the letter we want to send. 

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], msg=f"Subject: Happy Birthday\n\n {contents}")
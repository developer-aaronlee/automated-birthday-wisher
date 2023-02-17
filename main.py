##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import smtplib
import datetime as dt
import pandas
import random
import os

my_email = "pythonautomationapp@gmail.com"
password = "dxabiogqxlleamrw"

# now = dt.datetime.now()
# month = now.month
# day = now.day

# data = pandas.read_csv("birthdays.csv")
# birth_name = data.name
# birth_month = data.month
# birth_day = data.day
# birth_email = data.email

# for x in range(len(data.index)):
#     random_letter = random.choice(os.listdir("letter_templates"))
#     if birth_month[x] == month and birth_day[x] == day:
#         with open(f"letter_templates/{random_letter}") as file:
#             selected_letter = file.read()
#             formatted_letter = selected_letter.replace("[NAME]", birth_name[x])
#         with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#             connection.starttls()
#             connection.login(user=my_email, password=password)
#             connection.sendmail(from_addr=my_email, to_addrs=birth_email[x],
#                                 msg=f"Subject: Automation Test\n\n{formatted_letter}")

# data = pandas.read_csv("birthdays.csv")
# dict_data = data.to_dict(orient="records")
# print(dict_data)

# birth_name = data.name
# birth_month = data.month
# birth_day = data.day
# birth_email = data.email
# print(birth_email)

now = dt.datetime.now()
today = (now.month, now.day)
# print(today)

data = pandas.read_csv("birthdays.csv")
# print(data)
birth_dict = {(y.month, y.day): y for (x, y) in data.iterrows()}
# print(birth_dict[today])
if today in birth_dict:
    birth_person = birth_dict[today]
    # print(birth_person["name"])
    random_file = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(random_file) as file:
        selected_letter = file.read()
        formatted_letter = selected_letter.replace("[NAME]", birth_person["name"])
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=birth_person["email"],
                            msg=f"Subject: Happy Birthday\n\n{formatted_letter}")



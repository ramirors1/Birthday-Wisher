import smtplib
import random
import datetime

my_email = "pycharm454@gmail.com"
password = "zdvquzzqjnqggdac"
now = datetime.datetime.now()
weekday = now.weekday()
if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="pycharm454@yahoo.com",
            msg=f"Subject:Today's Motivation\n\n{quote}"
        )

print(weekday)


# import smtplib
#
# my_email = "pycharm454@gmail.com"
# password = "zdvquzzqjnqggdac"

# connection = smtplib.SMTP("smtp.gmail.com") # connects to email server
# connection.starttls()  # encrypts the connection to the email server
# connection.login(user=my_email, password=password)
# connection.sendmail(from_addr=my_email, to_addrs="pycharm454@yahoo.com", msg="Subject:Hello\n\nEmail body")
# connection.close()

# another way to write the code
# with smtplib.SMTP("smtp.gmail.com") as connection:  # connects to email server
#     connection.starttls()  # encrypts the connection to the email server
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="pycharm454@yahoo.com",
#         msg="Subject:Hello\n\nEmail body"
#     )

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(now)
#
# data_of_birth = dt.datetime(year=1980, month=1, day=15)
# print(data_of_birth)
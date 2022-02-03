import datetime as dt
import random
import smtplib
import ssl

my_email = "abahrom1700@gmail.com"
password = "20212022"
receiver = "bsayidbek@yahoo.com"

port = 587

weekdays = [day for day in range(0, 6)]

context = ssl.create_default_context()

now = dt.datetime.now()
weekday = now.weekday()
if weekday in weekdays:
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.ehlo()
        connection.starttls(context=context)
        connection.ehlo()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
                to_addrs=receiver,
                msg=f"Subject:Motivation\n\n{quote}"
            )

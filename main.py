import smtplib
import ssl


my_email = "abahrom1700@gmail.com"
password = ""
receiver = "sayidbekbakhrom@gmail.com"
port = 587

context = ssl.create_default_context()
try:
    with smtplib.SMTP("smtp.gmail.com", port) as connection:
        connection.ehlo()
        connection.starttls(context=context)
        connection.ehlo()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver,
            msg="Subject:Hello\n\nThis is the body of the email."
        )

except Exception as error:
    print(error)
finally:
    quit()

import datetime as dt

now = dt.datetime.now()
year = now.year
print(year)
date_of_birth = dt.datetime(year=2020, month=12, day=12)
print(date_of_birth)
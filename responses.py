import datetime as dt
import random


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hey"):
        return "Hello, how you doing?"

    if "how are you" in user_message:
        return "I am doing well thanks!"

    if "motivation" in user_message:
        with open("quotes.txt") as quote_files:
            all_quotes = quote_files.readlines()
            quote = random.choice(all_quotes)
        return f"{quote}"

    if user_message in ["who are you?", "who are you"]:
        return "I am telegram bot Rock 2022"

    if "time" in user_message:
        now = dt.datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)



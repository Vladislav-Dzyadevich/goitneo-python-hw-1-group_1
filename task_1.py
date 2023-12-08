from collections import defaultdict
from datetime import datetime, timedelta

def get_birthdays_per_week(users):
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)

        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days

        if delta_days < 7:
            day_of_week = (today + timedelta(days=delta_days)).strftime("%A")

            if day_of_week in ["Saturday", "Sunday"]:
                day_of_week = "Monday"

            birthdays_per_week[day_of_week].append(name)

    if not birthdays_per_week:
        print("На наступний тиждень немає днів народження.")
    else:
        for day, names in birthdays_per_week.items():
            print(f"{day}: {', '.join(names)}")

# Приклад використання:
users = [
    {"name": "Bill", "birthday": datetime(1955, 10, 28)},
    {"name": "Jan", "birthday": datetime(1976, 2, 24)},
    {"name": "Alice", "birthday": datetime(datetime.today().year, datetime.today().month, datetime.today().day + 3)},  
    {"name": "Vlad", "birthday": datetime(datetime.today().year, datetime.today().month, datetime.today().day + 5)}, 
    {"name": "Stepan", "birthday": datetime(datetime.today().year, datetime.today().month, datetime.today().day + 4)},
]

get_birthdays_per_week(users)

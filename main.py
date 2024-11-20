from datetime import datetime, timedelta, date


def string_to_date(date_string):
    date_date = datetime.strptime(date_string, '%Y.%m.%d')
    return date_date


def date_to_string(date):
    string_date = datetime.strftime(date, '%Y.%m.%d')
    return string_date


users = [
    {"name": "Bill Gates", "birthday": "1955.3.25"},
    {"name": "Steve Jobs", "birthday": "1955.3.21"},
    {"name": "Jinny Lee", "birthday": "1956.11.22"},
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"]).date()})
    return prepared_list


def find_next_weekday(start_date: datetime, weekday):
    start_date_weekday = start_date.weekday()
    time_delta = timedelta(days=weekday - start_date_weekday)
    if time_delta.days > 0:
        weekday_date = start_date + time_delta
    else:
        weekday_date = start_date + time_delta + timedelta(days=7)
    return weekday_date


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    prepared_users = prepare_user_list(users)
    for user in prepared_users:
        birthday_this_year = user['birthday'].replace(year=today.year)
        if birthday_this_year.month < today.month:
            birthday_this_year = birthday_this_year.replace(year=birthday_this_year.year+1)
        if 0 <= (birthday_this_year - today).days <= days:
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': date_to_string(birthday_this_year)})
    return upcoming_birthdays


def adjust_for_weekend(birthday: datetime):
    if birthday.weekday() >= 5:
        birthday = find_next_weekday(birthday, 0)
    return birthday


my_birthday = datetime(year=2003, month=11, day=23)
print(adjust_for_weekend(my_birthday))

print(get_upcoming_birthdays(users, 7))
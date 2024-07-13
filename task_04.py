from datetime import datetime, date, timedelta

def get_upcoming_birthdays(users):
    # current date and years
    today = date.today()
    current_year = datetime.now().year
    next_year = current_year + 1

    result = list()
    for user in users:
        # parse user birthday date
        user_birthday = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        user_month = user_birthday.month
        user_day = user_birthday.day
        
        # setup next birthdate date
        next_birthday = date(year=current_year, month=user_month, day=user_day)
        if next_birthday < today:
            next_birthday = date(year=next_year, month=user_month, day=user_day)

        diff_days = (next_birthday - today).days
        if diff_days < 7:
            # corrent date if weekends
            if next_birthday.weekday() in [5,6]:
                days_ahead = 7 - next_birthday.weekday()
                next_birthday = next_birthday + timedelta(days=days_ahead)
            
            congratulation_date = next_birthday.strftime('%Y.%m.%d')
            
            # add users with birthdays in this week
            data = {'name': user['name'], 'congratulation_date': congratulation_date}
            result.append(data)

    return result
    

users = [
    {"name": "Jane 2", "birthday": "1990.07.13"},
    {"name": "Jane 3", "birthday": "1990.07.17"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

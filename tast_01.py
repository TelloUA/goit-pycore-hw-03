from datetime import datetime, date
import re

input_string = input('Enter date in format YYYY-MM-DD: ')

def get_days_from_today(date_string: str) -> str:
    invalid_date_message = 'Invalid date: ' + date_string
    match = re.search(r'(\d{4})-(\d{2})-(\d{2})', date_string)

    if match is None:
        return invalid_date_message

    now = date.today()
    input_year = int(match.group(1))
    input_month = int(match.group(2))
    input_day = int(match.group(3))

    try:
        day = date(
            year=input_year,
            month=input_month, 
            day=input_day
            )
    except ValueError:
        return invalid_date_message
        
    diff = now - day
    diff_days = (str)(diff.days)

    return 'Difference between now and entered date: ' + diff_days + ' day(s)'

result = get_days_from_today(input_string)
print(result)

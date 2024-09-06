import requests
from datetime import datetime

base_url = "https://date.nager.at/api/v2"

def get_holidays(year, country_code):
    url = f"{base_url}/PublicHolidays/{year}/{country_code}"
    response = requests.get(url)
    return response.json()

def next_upcoming_holiday(holidays):
    today = datetime.now().date()
    future_holidays = [holiday for holiday in holidays if datetime.fromisoformat(holiday['date']).date() > today]
    future_holidays.sort(key=lambda x: x['date'])
    if future_holidays:
        next_holiday = future_holidays[0]
        return next_holiday
    return None

def count_holidays(holidays):
    return len(holidays)

def count_holidays_not_in_county(holidays, county_code):

    return count_holidays(holidays)

# holidays for canada
canadian_holidays = get_holidays(2017, 'CA')

# Q1: upcoming public holiday \
next_holiday = next_upcoming_holiday(canadian_holidays)
if next_holiday:
    holiday_name = next_holiday['localName']
    holiday_type = 'Fixed' if next_holiday['fixed'] else 'Not Fixed'
    print(f"{holiday_name}: {holiday_type}")
else:
    print("No upcoming holidays!")

# Q2: No. of public holidays in Canada - 2017

total_holidays = count_holidays(canadian_holidays)
print(f"No. of public holidays in Canada - 2017: {total_holidays}")

# Q3: Number of public holidays in Canada for 2017 that are not holidays in CA-BC county

holidays_not_in_county = count_holidays_not_in_county(canadian_holidays, 'CA-BC')
print(f"Number of public holidays in Canada in 2017, NOT holidays in CA-BC county: {holidays_not_in_county}")
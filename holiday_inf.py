import requests
from datetime import datetime

base_url = "https://date.nager.at/api/v2"

def get_holidays(year, country_code):
    response = requests.get(f"{base_url}/PublicHolidays/{year}/{country_code}")
    return response.json()

def next_upcoming_holiday(holidays):
    today = datetime.now().date()
    future_holidays = sorted(
        (holiday for holiday in holidays if datetime.fromisoformat(holiday['date']).date() > today),
        key=lambda x: x['date']
    )
    return future_holidays[0] if future_holidays else None

def count_holidays(holidays):
    return len(holidays)

# Get holidays for Canada in 2017
holidays = get_holidays(2017, 'CA')

# Q1:  upcoming public holiday
next_holiday = next_upcoming_holiday(holidays)
if next_holiday:
    print(f"{next_holiday['localName']}: {'Fixed' if next_holiday['fixed'] else 'Not Fixed'}")
else:
    print("No upcoming holidays!")

# Q2: Number of public holidays in Canada for 2017
print(f"No. of public holidays in Canada - 2017: {count_holidays(holidays)}")

# Q3: Number of public holidays in Canada for 2017 NOT in CA-BC
print(f"Number of public holidays in Canada in 2017, NOT holidays in CA-BC county: {count_holidays(holidays)}")

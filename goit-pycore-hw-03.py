from datetime import datetime #Завдання 1

def get_days_from_today(date:str)->int:
    try:
        date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        delta = today - date
        return delta.days 
    except ValueError:
        return "Невірний формат дати. Використовуйте 'YYYY-MM-DD'." 

result = get_days_from_today("2024-10-09")
print("result", result)

import random #Завдання 2
def get_numbers_ticket(min:int,max:int,quntity:int)->list:
    if min<1 or max>1000 or quntity<1 or quntity>(max-min+1):
        return "Некоректні вхідні дані"
    numbers=random.sample(range(min, max + 1), quntity)
    return sorted(numbers)  
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

import re #Завдання 3
def normalize_phone_number(phone:str)->str:
    telephone = re.sub(r"[^\d+]", "", phone.strip())
    if telephone.startswith("380"):
        return "+" + telephone
    elif telephone.startswith("0"):
        return "+38" + telephone
    else:
        return "+380" + telephone
wright_number = normalize_phone_number("0932836370")
print("Нормалізований номер телефону:", wright_number)

from datetime import datetime, timedelta #Завдання 4
def get_upcoming_birthdays(users:list)->list: 
    today=datetime.today().date()
    upcoming_birthdays=[]
    for user in users:
        name=user["name"]
        birthday=datetime.strptime(user["birthday"], "%Y-%m-%d").date()
        birthday_this_year=birthday.replace(year=today.year)
        if birthday_this_year<today:
            birthday_this_year=birthday_this_year.replace(year=today.year+1)
        days_until_birthday=(birthday_this_year-today).days
        if 0 <= days_until_birthday <= 7:
          congratulation_date = birthday_this_year
    if congratulation_date.weekday() == 5:  # субота
        congratulation_date += timedelta(days=2)
    elif congratulation_date.weekday() == 6:  # неділя
        congratulation_date += timedelta(days=1)
    upcoming_birthdays.append({
        "name": name,
        "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
    })
    return upcoming_birthdays
users = [{"name": "Марія", "birthday": "1992-10-13"},]
result = get_upcoming_birthdays(users)
print("result", result)
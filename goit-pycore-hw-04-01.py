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

def get_upcoming_birthday(users:dict, birthday:str)->str: #Завдання 4
    try:
        birth_date = datetime.strptime(birth_date, "%Y-%m-%d").date()
        today = datetime.today().date()
        current_year_birthday = today+7
        if today==current_year_birthday:
            current_year_birthday = current_year_birthday.replace(year=today.year + 1)
        days_until_birthday = (current_year_birthday - today).days
        return f"До наступного дня народження залишилось {days_until_birthday} днів."
    except ValueError:
        return "Невірний формат дати. Використовуйте 'YYYY-MM-DD'."
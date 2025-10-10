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
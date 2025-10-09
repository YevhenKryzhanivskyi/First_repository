from datetime import datetime

now = datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

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
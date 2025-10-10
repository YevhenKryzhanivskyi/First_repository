import random #Завдання 2
def get_numbers_ticket(min:int,max:int,quntity:int)->list:
    if min<1 or max>1000 or quntity<1 or quntity>(max-min+1):
        return "Некоректні вхідні дані"
    numbers=random.sample(range(min, max + 1), quntity)
    return sorted(numbers)  
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)
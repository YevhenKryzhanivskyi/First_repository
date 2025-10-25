import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]: #Генерує всі дійсні числа з тексту, які чітко відокремлені пробілами.
    
    pattern = r'\s(\d+\.\d+)\s' # Регулярний вираз для пошуку чисел, відокремлених пробілами

    
    for match in re.finditer(pattern, text): # Ітеруємо по всіх збігах у тексті
        yield float(match.group(1))# Перетворюємо знайдене число на float і повертаємо через yield


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:  #Обчислює загальну суму дійсних чисел у тексті, використовуючи генератор.  
      
    return sum(func(text))  # Викликаємо генератор і підсумовуємо всі його значення


def read_text_from_file(file_path: str) -> str:
       
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл не знайдено: {file_path}")
        return ""
    except Exception as e:
        print(f"Помилка при читанні файлу: {e}")
        return ""


def main(): #Основна функція для виконання програми
    file_path = "income_data.txt"
    text = read_text_from_file(file_path)  # Зчитуємо текст із файлу
 
    if text:# Перевіряємо, чи текст не порожній
        
        total_income = sum_profit(text, generator_numbers) # Обчислюємо загальний прибуток
        print(f"Загальний дохід: {total_income}")  # Виводимо результат
    else:
        print("Неможливо обробити порожній текст.")


if __name__ == "__main__": # Перевірка, чи файл запущено напряму
    main()
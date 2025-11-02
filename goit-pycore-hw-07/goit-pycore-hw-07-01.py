from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value):
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        if not value.isdigit() or len(value) != 10:
            raise ValueError("Телефонний номер повинен містити 10 цифр.")


class Birthday(Field):
    def __init__(self, value):
        try:
            parsed_date = datetime.strptime(value, "%d.%m.%Y")
            super().__init__(parsed_date)
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуйте DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    def add_phone(self, phone_number):
        phone = Phone(phone_number)
        self.phones.append(phone)

    def remove_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                self.phones.remove(phone)
                return True
        return False

    def edit_phone(self, old_number, new_number):
        for index, phone in enumerate(self.phones):
            if phone.value == old_number:
                self.phones[index] = Phone(new_number)
                return True
        return False

    def find_phone(self, phone_number):
        for phone in self.phones:
            if phone.value == phone_number:
                return phone
        return None

    def add_birthday(self, birthday_str):
        self.birthday = Birthday(birthday_str)

    def __str__(self):
        phones_str = '; '.join(phone.value for phone in self.phones)
        birthday_str = (
            self.birthday.value.strftime("%d.%m.%Y")
            if self.birthday else "не вказано"
        )
        return (
            f"Ім'я контакту: {self.name.value}, "
            f"телефони: {phones_str}, "
            f"день народження: {birthday_str}"
        )


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
            return True
        return False

    def get_upcoming_birthdays(self):
        today = datetime.today().date()
        upcoming_birthdays = []

        for record in self.data.values():
            if record.birthday:
                birthday = record.birthday.value.date()
                birthday_this_year = birthday.replace(year=today.year)

                if birthday_this_year < today:
                    birthday_this_year = birthday_this_year.replace(
                        year=today.year + 1)

                days_until_birthday = (birthday_this_year - today).days

                if 0 <= days_until_birthday <= 7:
                    congratulation_date = birthday_this_year

                    if congratulation_date.weekday() == 5:
                        congratulation_date += timedelta(days=2)
                    elif congratulation_date.weekday() == 6:
                        congratulation_date += timedelta(days=1)

                    date_str = congratulation_date.strftime("%Y.%m.%d")
                    upcoming_birthdays.append({
                        "name": record.name.value,
                        "congratulation_date": date_str
                    })

        return upcoming_birthdays


if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_birthday("01.11.1990")
    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_birthday("08.11.1995")
    book.add_record(jane_record)

    print("Всі записи в адресній книзі:")
    for record in book.data.values():
        print(record)

    john = book.find("John")
    if john:
        john.edit_phone("1234567890", "1112223333")
        print("\nПісля редагування телефону John:")
        print(john)

        found_phone = john.find_phone("5555555555")
        print(f"\nЗнайдено телефон у John: {found_phone}")
    else:
        print("Контакт John не знайдено.")

    deleted = book.delete("Jane")
    print("\nЗапис Jane видалено." if deleted else "Запис Jane не знайдено.")

    print("\nПривітання на наступному тижні:")
    birthdays = book.get_upcoming_birthdays()
    for entry in birthdays:
        print(f"{entry['name']} — привітати {entry['congratulation_date']}")

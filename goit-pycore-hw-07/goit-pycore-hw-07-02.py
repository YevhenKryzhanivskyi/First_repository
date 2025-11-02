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
        value = value.strip()
        self.validate(value)
        super().__init__(value)

    @staticmethod
    def validate(value):
        value = value.strip()
        if (not value.isdigit()
                or len(value) != 10
                or not value.startswith("0")):
            raise ValueError(
                "Телефонний номер повинен містити 10 цифр і починатися з 0."
            )


class Birthday(Field):
    def __init__(self, value):
        try:
            parsed_date = datetime.strptime(value.strip(), "%d.%m.%Y")
            super().__init__(parsed_date)
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуйте DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name.strip())
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
        return self.data.get(name.strip())

    def delete(self, name):
        name = name.strip()
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
                        year=today.year + 1
                    )

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


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, KeyError, ValueError) as e:
            return f"Помилка: {e}"
    return wrapper


@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def add_birthday(args, book):
    name, birthday_str = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday_str)
        return f"День народження для {name} додано: {birthday_str}"
    return f"Контакт з ім'ям {name} не знайдено."


@input_error
def show_birthday(args, book):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return (
            f"День народження {name}: "
            f"{record.birthday.value.strftime('%d.%m.%Y')}"
        )
    if record:
        return f"Для контакту {name} день народження не вказано."
    return f"Контакт з ім'ям {name} не знайдено."


@input_error
def birthdays(args, book):
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "Немає привітань на наступному тижні."
    result = "Привітання на наступному тижні:\n"
    for entry in upcoming:
        result += (
            f"{entry['name']} — привітати {entry['congratulation_date']}\n"
        )
    return result.strip()


def parse_input(user_input):
    parts = user_input.strip().split()
    return parts[0], parts[1:]


def main():
    book = AddressBook()
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            name, old_phone, new_phone = args
            record = book.find(name)
            if record and record.edit_phone(old_phone, new_phone):
                print(
                    f"Телефон {old_phone} змінено на {new_phone} "
                    f"для контакту {name}."
                )
            else:
                print(f"Не вдалося змінити телефон для {name}.")

        elif command == "phone":
            name = args[0]
            record = book.find(name)
            if record:
                phones = ', '.join(phone.value for phone in record.phones)
                print(f"Телефони {name}: {phones}")
            else:
                print(f"Контакт з ім'ям {name} не знайдено.")

        elif command == "all":
            if not book.data:
                print("Адресна книга порожня.")
            else:
                for record in book.data.values():
                    print(record)

        elif command == "add-birthday":
            print(add_birthday(args, book))

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(birthdays(args, book))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

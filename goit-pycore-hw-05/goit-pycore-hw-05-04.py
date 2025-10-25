contacts = {}


def input_error(func):
    """
    Декоратор для обробки помилок введення користувача.
    """
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Enter the argument for the command."
    return inner


def parse_input(user_input):
    """
    Розділяє введення користувача на команду та аргументи.
    """
    parts = user_input.strip().split()
    if not parts:
        return "", []
    command = parts[0].lower()
    args = parts[1:]
    return command, args


@input_error
def add_contact(args):
    """
    Додає новий контакт до словника.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."


@input_error
def change_contact(args):
    """
    Змінює номер телефону для існуючого контакту.
    """
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Contact updated."
    else:
        raise KeyError


@input_error
def show_phone(args):
    """
    Показує номер телефону для заданого імені.
    """
    name = args[0]
    return contacts[name]


@input_error
def show_all():
    """
    Виводить усі збережені контакти.
    """
    if not contacts:
        return "No contacts found."
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])


def show_help():
    """
    Показує список доступних команд.
    """
    return """Available commands:
  hello
  add [name] [phone]
  change [name] [new_phone]
  phone [name]
  all
  help
  exit / close"""


def main():
    """
    Основна функція для запуску бота.
    """
    print("Welcome to Assistant Bot! Type 'help' for commands.")
    while True:
        user_input = input(">>> ")
        command, args = parse_input(user_input)

        if command in ("exit", "close"):
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args))
        elif command == "change":
            print(change_contact(args))
        elif command == "phone":
            print(show_phone(args))
        elif command == "all":
            print(show_all())
        elif command == "help":
            print(show_help())
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
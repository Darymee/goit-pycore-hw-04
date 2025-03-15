def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def validate_name(name):
    return isinstance(name, str)


def validate_phone(phone):
    return phone.isdigit()


def add_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide a name and phone number."

    name, phone = args

    if not validate_name(name):
        return "Invalid name. Name must be a string."

    if not validate_phone(phone):
        return "Invalid phone number. Phone number must contain only digits."

    if name in contacts:
        return "Contact with this name already exist."

    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Invalid command. Please provide a name and a new phone number."

    name, phone = args

    if not validate_name(name):
        return "Invalid name. Name must be a string."
    if not validate_phone(phone):
        return "Invalid phone number. Phone number must contain only digits."

    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact not found."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Invalid command. Please provide a name."

    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}."
    else:
        return "Contact not found."


def show_all(contacts):
    if not contacts:
        return "No contacts found."

    contact_list = "\n".join(f"{name}: {phone}" for name, phone in contacts.items())
    return contact_list


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()

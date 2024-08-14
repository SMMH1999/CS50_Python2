import os


ledger = []


def main():
    # Function for sorting dictionary base on 'name' and 'username'
    def sortkey(obj) -> str:
        return f'{obj["name"]}{obj["username"]}'

    while True:
        ledger.sort(key=sortkey)
        action = gui()
        if action == 1:
            # Action 1 for Add Item to ledger
            add(get_data("For Adding Item".title()))
        elif action == 2:
            # Action 2 for Remove Item from ledger
            remove(get_data("For Removing specific Item".title()))
        elif action == 3:
            # Action 3 for Show Items in ledger
            show()


def get_data(title: str) -> dict:
    get_input_error = ""
    name = None
    username = None
    password = None
    while True:
        os.system("cls")
        try:
            print(f"{'Getting Data ' + title}\n\n{get_input_error}")
            if name is None:
                name = input(
                    "Enter the name of Application, Website, Account or etc : "
                ).capitalize()

                if not name:
                    name = None
                    raise ValueError(
                        "The name of Application, Website, Account or etc can not be empty !!\n"
                    )

            if username is None:
                username = input(f"Enter the Username for '{name}' : ")
                if not username:
                    username = None
                    raise ValueError(f"The Username for '{name}' can not be empty !!\n")

            if password is None:
                password = input(
                    f"Enter the Password for '{username}' in '{name}' or (Re-enter '{username}' for change it) : "
                )
                if not password:
                    password = None
                    raise ValueError(
                        f"The Password for '{username}' in '{name}' can not be empty !!\n"
                    )

                if username == password:
                    error_message = f"Username and Password are the same, '{username}' == '{password}' is not acceptable \n"
                    username = None
                    password = None
                    raise ValueError(error_message)

            data_obj = {"name": name, "username": username, "password": password}
            return data_obj
        except ValueError as input_error:
            get_input_error = input_error


def gui() -> int:
    error_message = ""
    while True:
        os.system("cls")
        print(f"{'*' * 60}")
        print(f"*{'Welcome To Password Manager Python Application': ^58}*")
        print(f"{'*' * 60}")
        print(f"*{'1 => Add Item': ^58}*")
        print(f"*{'2 => Remove Item': ^58}*")
        print(f"*{'3 => Show Items': ^58}*")
        print(f"{'*' * 60}")
        try:
            entered_number = input(
                f"\n{error_message}\nSelect the action number to execute: "
            )
            if entered_number:
                entered_number = int(entered_number)
                if entered_number in range(1, 4):
                    return entered_number
                raise IndexError("The action number to execute is out of range !!\n")
            raise ValueError("The action number to execute can not be empty !!\n")
        except (ValueError, IndexError) as entered_number_error:
            error_message = entered_number_error


def valid_object(obj: dict) -> bool:
    try:
        keys = list(obj.keys())
    except Exception:
        return False

    if len(keys) != 3:
        return False

    for item in ["name", "username", "password"]:
        if item not in keys:
            return False

    return True


def add(obj: dict) -> bool:
    if valid_object(obj):
        try:
            ledger.index(obj)
        except ValueError:
            ledger.append(obj)
            return True

        raise ValueError("This information are existed")

    raise ValueError("Your input is not enough")


def edit(obj, new_obj) -> bool:
    if obj == new_obj:
        raise ValueError("New information are the same last information")
    if valid_object(obj) and valid_object(new_obj):
        try:
            find_obj = search(obj)
            index_obj = ledger.index(find_obj)
        except ValueError as find_error:
            raise ValueError("Your information not existed !!") from find_error

        for key, value in new_obj.items():
            ledger[index_obj][key] = value

        return True

    raise ValueError("Your input not enough !!")


def show() -> bool:
    error_message = ""
    if len(ledger):
        os.system("cls")

        print(f"\n{'All information': ^66}\n")
        print(f"|{'-' * 6}+{'-' * 19}+{'-' * 18}+{'-' * 19}|")
        print(f"|{'Row': ^6}|{'Name': ^19}|{'Username': ^18}|{'Password': ^19}|")
        print(f"|{'-' * 6}+{'-' * 19}+{'-' * 18}+{'-' * 19}|")

        for index, obj in enumerate(ledger):
            print(
                f"|{index+1: ^6}|{obj['name']: ^19}|{obj['username']: ^18}|{obj['password']: ^19}|"
            )
            print(f"|{'-' * 6}+{'-' * 19}+{'-' * 18}+{'-' * 19}|")
        # os.system("cls")
        try:
            row = input(
                f"\n{error_message}\nif want to Edit any item enter the row (0 for came back):"
            )
            if not row or row == "0":
                return True

            row_index = int(row) - 1
            if row_index in range(len(ledger) + 1):
                edit(ledger[row_index], get_data("For Editing specific Item".title()))
                return True

            raise IndexError(f"Entered row is out of range [1, {len(ledger) + 1}] !!\n")
        except (ValueError, IndexError) as edit_error:
            error_message = edit_error
    else:
        raise ValueError("The ledger is empty!!")


def remove(obj: dict) -> bool:
    if valid_object(obj):
        try:
            obj_index = ledger.index(obj)
        except ValueError as index_error:
            raise ValueError("Your information dose not exist") from index_error

        ledger.pop(obj_index)
        return True
    raise ValueError("Your information can not be empty !!")


def search(obj) -> dict:
    if not obj:
        raise ValueError("Object can not be empty!")

    try:
        item = ledger.index(obj)
    except:
        raise ValueError("Item not existed")

    return ledger[item]


if __name__ == "__main__":
    main()

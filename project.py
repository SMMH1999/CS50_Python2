import os


ledger = []


def main():
    data = {"name": "GitHub", "username": "User1", "password": "PassWord1"}
    add(data)
    # add(data)
    # search(data)
    show()
    new_date = {"name": "GitLab", "username": "User1", "password": "PassWord1"}
    edit(data, new_date)
    show()
    remove(new_date)


def add(obj):
    if obj:
        try:
            find_obj = ledger.index(obj)
        except ValueError:
            find_obj = -1

        if find_obj == -1:
            ledger.append(obj)
            return True

        raise ValueError("This information are existed")

    raise ValueError("Your input is not enough")


def edit(obj, new_obj) -> bool:
    if obj and new_obj:
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

    if len(ledger):
        os.system("cls")

        print("\nThis is your Ledger:\n")
        print(f"{'-' * 50}")
        for obj in ledger:
            print(
                f"\nin {obj['name']}, your Username: {obj['username']} and Password: {obj['password']}"
            )
        # os.system("cls")
        return True
    else:
        raise ValueError("The ledger is empty!!")


def remove(obj):
    if obj:
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

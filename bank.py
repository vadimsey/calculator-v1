import json

def main():
    choice()


def choice():
    print("1. Create a new account")
    print("2. View a new accounts")

    choice = input("Choice the number: ")
    if choice == "1":
        new_account()
    if choice == "2":
        view_accounts()

def view_accounts():
    with open("accounts.json", "r") as json_file:
        data = json.load(json_file)
    for n, b in data.items():
        print(f"Name:{n}, Balance:{b}")


def new_account():
    l = []
    try:
        with open("accounts.json","r") as file:
            data = json.load(file)
            if len(data.keys()) == 3:
                print("=====YOU HAVE 3 ACCOUNTS=====")
                choice()
    except:
        data = []


    print("You can create max 3 accounts")
    create = input("Do you want to create another account? (y/n)")
    if create == "y":
        create_account()
    if create == "n":
        choice()


def create_account():
    account = input("Enter new account name: ")
    while True:
        try:
            balance = int(input("Enter your balance: "))
            if balance < 0:
                print("Please enter a positive number")
            else:
                pass

        except:
            print("====Please enter a number====")
        else:
            break

    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        accounts = {}

    accounts[account] = balance

    with open("accounts.json", "w") as file:
        json.dump(accounts, file)

    choice()


if __name__ == "__main__":
    main()
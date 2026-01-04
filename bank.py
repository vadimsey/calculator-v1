import json

class Account:
    def __init__(self, holder, balance, account_number):
        self._holder = holder
        self._balance = balance
        self._account_number = account_number

    @property
    def holder(self):
        return self._holder

    @holder.setter
    def holder(self, value):
        for i in value:
            if i.isdigit():
                print("=====NAME MUST NOT CONTAIN DIGITS=====")
            else:
                holder = value

    @property
    def balance(self):
        return self._balance

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if value.isdigit():
            self._account_number = value
            print(f"=====ACCOUNT NUMBER UPDATED TO {value}")
        else:
            print("=====ERROR=====")

    def deposit(self, amount):
        if amount < 0:
            print("=====AMOUNT MUST BE POSITIVE=====")
        else:
            self._balance += amount
            print(f"=====DEPOSIT: {amount}=====")

    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            print(f"=====WITHDRAW: {amount}=====")
        else:
            print("=====ERROR AMOUNT=====")

    def __str__(self):
        return f"ACCOUNT #{self.account_number} Holder: {self.holder} Balance: {self.balance}"

class SavingsAccount(Account):
    def __init__(self, holder, balance, account_number, interest_rate=0.05):
        super().__init__(holder, balance, account_number)
        self.interest_rate = interest_rate

    def apply_interest(self):
        self._balance = self._balance + self._balance * self.interest_rate
        print(f"=====SAVINGS: {self.interest_rate}=====")

class Bank:
    def __init__(self):
        self._accounts = []
        self.load_account()

    def _find_account(self, number):
        i = None
        for acc in self._accounts:
            if acc.account_number == number:
                i = acc

        if i != None:
            return i
        else:
            print("=====NUMBER NOT FOUND=====")
            return None


    def save_account(self):
        data = []
        for acc in self._accounts:
            acc_data = {
                "holder": acc.holder,
                "balance": acc.balance,
                "account_number": acc.account_number,
                "type": "Savings" if isinstance(acc, SavingsAccount) else "Basic",
            }
            data.append(acc_data)
        with open("accounts.json", "w") as file:
            json.dump(data, file)

    def load_account(self):
        try:
            with open("accounts.json", "r") as file:
                data = json.load(file)
                self._accounts = []
                for item in data:
                    if item["type"] == "Savings":
                        acc = SavingsAccount(item["holder"], item["balance"], item["account_number"])
                    else:
                        acc = Account(item["holder"], item["balance"], item["account_number"])
                    self._accounts.append(acc)
        except (FileNotFoundError, json.JSONDecodeError):
            self._accounts = []

    def view_accounts(self):
        self.load_account()
        self.sort_accounts()
        for acc in self._accounts:
            print(f"Holder: {acc.holder}, Balance: {acc.balance}, Account Number: {acc.account_number}")

    def add_account(self, acc):
        if acc in self._accounts:
            print("=====ACCOUNT ALREADY ADDED=====")
        else:
            self._accounts.append(acc)
            print(f"ACCOUNT ADDED: {acc}")

    def transfer(self, from_number, to_number, amount):
        self.load_account()

        sender = self._find_account(from_number)
        receiver = self._find_account(to_number)

        if sender is None or receiver is None:
            print("===== ERROR: ONE OR BOTH ACCOUNTS NOT FOUND =====")
            return

        if amount > sender.balance:
            print("===== ERROR: INSUFFICIENT FUNDS =====")
            return

        sender.withdraw(amount)
        receiver.deposit(amount)

        print(f"===== SUCCESSFUL TRANSFER: {amount} =====")
        self.save_account()

    def sort_accounts(self):
        self._accounts.sort(key=lambda acc: acc.balance, reverse=True)

    def deposit(self, number, amount):
        account = self._find_account(number)
        account.deposit(amount)
        self.save_account()

    def withdraw(self, number, amount):
        account = self._find_account(number)
        account.withdraw(amount)
        self.save_account()


def create_account():
    while True:
        try:
            holder = input("Enter Holder: ")
            balance = int(input("Enter Balance: "))
            account_number = int(input("Enter Account Number: "))
        except KeyboardInterrupt:
            print("=====ERROR=====")
            continue
        else:
            break

    return Account(holder, balance, account_number)

def main():
    bank = Bank()

    while True:
        print("=====MENU=====")
        print("1. ADD ACCOUNT", "\n2. TRANSFER", "\n3. SORT ACCOUNTS", "\n4. VIEW ACCOUNTS", "\n5. DEPOSIT", "\n6. WITHDRAW", "\n7. EXIT")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("=====ERROR=====")
            continue

        if choice == 1:
            bank.add_account(create_account())
        elif choice == 2:
            index1 = int(input("Enter account from transfer: "))
            index2 = int(input("Enter account to transfer: "))
            amount = int(input("Enter amount to transfer: "))

            bank.transfer(index1, index2, amount)
        elif choice == 3:
            bank.sort_accounts()
        elif choice == 4:
            bank.view_accounts()
        elif choice == 5:
            try:
                number = int(input("Enter account number: "))
                amount = int(input("Enter amount to deposit: "))
            except ValueError:
                print("=====ERROR=====")
                continue
            bank.deposit(number, amount)
        elif choice == 6:
            try:
                number = int(input("Enter account number: "))
                amount = int(input("Enter amount to deposit: "))
            except ValueError:
                print("=====ERROR=====")
                continue
            bank.withdraw(number, amount)
        elif choice == 7:
            break
        else:
            print("=====ENTER CORRECT CHOICE=====")
            continue

if __name__ == "__main__":
    main()

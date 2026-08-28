import json


class PasswordManager:

    def __init__(self):
        self.accounts = []

    def add_account(self):
        account = input("Account name: ")
        password = input("Password: ")

        new_account = {
            "account": account,
            "password": password
        }

        self.accounts.append(new_account)

        print("Account added successfully!")

    def show_accounts(self):
        if not self.accounts:
            print("No accounts found.")
            return

        print("\n====== Accounts ======")

        for i, account in enumerate(self.accounts, start=1):
            print(f"{i}. {account['account']}")

    def search_account(self):
        name = input("Which account do you want to search for? ")

        for account in self.accounts:
            if account["account"].lower() == name.lower():
                print(f"Account: {account['account']}")
                print(f"Password: {account['password']}")
                return

        print("Account not found.")

    def delete_account(self):
        name = input("Which account do you want to delete? ")

        for account in self.accounts:
            if account["account"].lower() == name.lower():
                self.accounts.remove(account)
                print("Account deleted successfully!")
                return

        print("Account not found.")

    def save(self):
        with open("passwords.json", "w") as file:
            json.dump(self.accounts, file, indent=4)

        print("Accounts saved.")

    def load(self):
        try:
            with open("passwords.json", "r") as file:
                self.accounts = json.load(file)

        except FileNotFoundError:
            self.accounts = []


def main():

    manager = PasswordManager()

    manager.load()

    while True:

        print("""
====== Password Manager ======

1. Add account
2. Show accounts
3. Search
4. Delete
5. Exit
""")

        choice = input("Choose: ")

        if choice == "1":
            manager.add_account()

        elif choice == "2":
            manager.show_accounts()

        elif choice == "3":
            manager.search_account()

        elif choice == "4":
            manager.delete_account()

        elif choice == "5":
            manager.save()
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()


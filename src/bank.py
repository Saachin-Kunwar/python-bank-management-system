import json
import os
from src.account import Account

class Bank:
    def __init__(self):
        self.accounts = {}

        self.base_dir = os.path.dirname(os.path.dirname(__file__))
        self.data_file = os.path.join(self.base_dir, "data", "bank_data.json")

        self.load_data()

    # ---------------- CREATE ACCOUNT ----------------
    def create_account(self):
        name = input("Enter name: ")
        pin = input("Set PIN: ")

        if name in self.accounts:
            print("❌ Account already exists")
        else:
            self.accounts[name] = Account(name, pin)
            print("✅ Account created")
            self.save_data()

    # ---------------- LOGIN ----------------
    def login(self):
        name = input("Enter name: ")
        pin = input("Enter PIN: ")

        acc = self.accounts.get(name)

        if acc and acc.pin == pin:
            if not acc.is_active:
                print("❌ Account is deactivated")
                return

            print(f"✅ Welcome {name}")
            self.account_menu(acc)
        else:
            print("❌ Invalid credentials")

    # ---------------- MENU ----------------
    def account_menu(self, acc):
        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Balance")
            print("4. History")
            print("5. Transfer Money 💸")
            print("6. Deactivate Account")
            print("7. Delete Account")
            print("8. Logout")

            choice = input("Choose: ")

            if choice == "1":
                acc.deposit(float(input("Amount: ")))

            elif choice == "2":
                acc.withdraw(float(input("Amount: ")))

            elif choice == "3":
                acc.check_balance()

            elif choice == "4":
                acc.show_history()

            elif choice == "5":
                self.transfer_money(acc)

            elif choice == "6":
                self.deactivate_account(acc)
                break

            elif choice == "7":
                if self.delete_account(acc):
                    break

            elif choice == "8":
                self.save_data()
                print("👋 Logged out")
                break

            else:
                print("❌ Invalid choice")

    # ---------------- TRANSFER MONEY ----------------
    def transfer_money(self, sender):
        receiver_name = input("Enter receiver name: ")
        amount = float(input("Enter amount: "))

        receiver = self.accounts.get(receiver_name)

        if not receiver:
            print("❌ Receiver not found")
            return

        if amount > sender.balance:
            print("❌ Insufficient balance")
            return

        sender.send_money(amount, receiver_name)
        receiver.add_money(amount, sender.name)

        print(f"✅ {amount} transferred to {receiver_name}")

        self.save_data()

    # ---------------- DEACTIVATE ----------------
    def deactivate_account(self, acc):
        acc.is_active = False
        self.save_data()
        print("⚠️ Account deactivated")

    # ---------------- DELETE ----------------
    def delete_account(self, acc):
        confirm = input("Type 'DELETE' to confirm: ")

        if confirm == "DELETE":
            del self.accounts[acc.name]
            self.save_data()
            print("🗑️ Account deleted")
            return True
        else:
            print("❌ Cancelled")
            return False

    # ---------------- REACTIVATE ----------------
    def reactivate_account(self):
        name = input("Enter account name: ")
        pin = input("Enter PIN: ")

        acc = self.accounts.get(name)

        if acc and acc.pin == pin:
            if acc.is_active:
                print("✅ Account already active")
            else:
                acc.is_active = True
                self.save_data()
                print("✅ Account reactivated")
        else:
            print("❌ Invalid credentials")

    # ---------------- SAVE DATA ----------------
    def save_data(self):
        data = {}

        for name, acc in self.accounts.items():
            data[name] = {
                "pin": acc.pin,
                "balance": acc.balance,
                "history": acc.history,
                "is_active": acc.is_active
            }

        os.makedirs(os.path.dirname(self.data_file), exist_ok=True)

        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    # ---------------- LOAD DATA ----------------
    def load_data(self):
        try:
            with open(self.data_file, "r") as f:
                data = json.load(f)

                for name, info in data.items():
                    acc = Account(name, info["pin"], info["balance"])
                    acc.history = info["history"]
                    acc.is_active = info.get("is_active", True)
                    self.accounts[name] = acc

        except FileNotFoundError:
            pass
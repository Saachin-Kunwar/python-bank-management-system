from datetime import datetime

class Account:
    def __init__(self, name, pin, balance=0):
        self.name = name
        self.pin = pin
        self.balance = balance
        self.history = []
        self.is_active = True

    def deposit(self, amount):
        self.balance += amount
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"Deposited {amount} at {time}")
        print("✅ Deposited successfully")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.history.append(f"Withdrawn {amount} at {time}")
            print("✅ Withdraw successful")
        else:
            print("❌ Insufficient balance")

    def add_money(self, amount, sender_name):
        self.balance += amount
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"Received {amount} from {sender_name} at {time}")

    def send_money(self, amount, receiver_name):
        self.balance -= amount
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(f"Sent {amount} to {receiver_name} at {time}")

    def check_balance(self):
        print(f"💰 Balance: {self.balance}")

    def show_history(self):
        print("📜 Transaction History:")
        for h in self.history:
            print("-", h)
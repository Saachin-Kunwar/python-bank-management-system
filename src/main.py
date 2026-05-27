from src.bank import Bank

def main():
    bank = Bank()

    while True:
        print("\n===== BANK SYSTEM =====")
        print("1. Create Account")
        print("2. Login")
        print("3. Reactivate Account")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.login()

        elif choice == "3":
            bank.reactivate_account()

        elif choice == "4":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    main()
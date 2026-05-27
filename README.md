<p align="center">
  A modern <b>Bank Management System</b> built using <b>Python</b> featuring account management, transaction history, money transfer system, account activation controls, and persistent JSON-based storage using modular project architecture.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-Programming-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/OOP-Architecture-success?style=for-the-badge">
  <img src="https://img.shields.io/badge/JSON-Storage-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/System-Banking-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
</p>

---

# 🏦 Bank Management System

A modular **Bank Management System** developed using Python implementing account creation, transaction management, fund transfer system, account lifecycle handling, and persistent data storage.

This project focuses not only on banking operations but also on learning **project structure, modular architecture, OOP concepts, file handling, and maintainable code organization**.

---

## 🚀 Features

### 👤 Account Management System

- Create new account
- Secure PIN authentication
- Login system
- Account reactivation
- Account deletion
- Active / Inactive account status management

---

## 💰 Banking Operations

### Deposit System

- Add money to account
- Automatic balance updates
- Transaction recording
- Timestamp generation

### Withdraw System

- Withdraw available balance
- Insufficient balance validation
- Auto transaction logging

---

## 💸 Money Transfer System

Features:

✅ Send money between users

✅ Receiver validation

✅ Balance checking

✅ Sender history update

✅ Receiver history update

✅ Automatic save operation

Example Flow:

```bash
Hari → Send Rs 5000 → Ram
```

History Generated:

```bash
Sent 5000 to Ram
Received 5000 from Hari
```

---

## 📜 Transaction History System

Tracks all activities:

- Deposits
- Withdrawals
- Transfers
- Received money

Example:

```bash
Deposited 5000 at 2026-05-27 10:15:00

Withdrawn 1000 at 2026-05-27 10:30:12

Sent 500 to Ram at 2026-05-27 11:00:18

Received 500 from Hari at 2026-05-27 11:00:18
```

---

## ⚠ Account Lifecycle Management

### Deactivate Account

- Temporarily disables account
- Login restriction applied

### Reactivate Account

- Restore account access
- PIN verification required

### Delete Account

- Permanent removal
- Confirmation required

```bash
Type DELETE to confirm
```

---

## 💾 Persistent Data Storage

This project uses:

```python
JSON Storage
```

Stored Information:

- User PIN
- Balance
- Transaction History
- Account Status

Features:

✅ Auto Save

✅ Auto Load

✅ Persistent storage

✅ File-based database approach

Storage File:

```bash
data/bank_data.json
```

---

# 🧠 OOP Concepts Used

## Account Class

Responsible for:

- Deposits
- Withdrawals
- Transfers
- History management
- Balance operations

Methods:

```python
deposit()

withdraw()

send_money()

add_money()

check_balance()

show_history()
```

---

## Bank Class

Responsible for:

- Authentication
- Account creation
- Transfer handling
- Persistence layer
- Lifecycle management

Methods:

```python
create_account()

login()

transfer_money()

deactivate_account()

delete_account()

reactivate_account()

save_data()

load_data()
```

---

## 📂 Project Structure

```bash
BANK-MANAGEMENT-SYSTEM/
│
├── data/
│   └── bank_data.json
│
├── src/
│   ├── __init__.py
│   ├── account.py
│   ├── bank.py
│   └── main.py
│
├── .gitignore
└── venv/
```

---

## ⚙️ Technologies Used

### Programming

- Python

### Concepts

- Object Oriented Programming (OOP)
- Modular Programming
- File Handling
- Authentication Logic

### Modules

- JSON
- Datetime
- OS

---

## 🧠 Concepts Learned

### Python Development

- Classes & Objects
- Encapsulation
- Package Structure
- Modular Architecture
- Import System

### System Design

- Authentication flow
- State management
- Transaction management
- Persistence layer

### File Handling

- JSON serialization
- Data loading
- File operations
- Path management

---

## ⚠ Challenges Faced

### Project Architecture

- Organizing project folders
- Separating logic into modules
- Managing imports

Example:

```python
from src.account import Account
```

---

### Persistence Layer

Problems:

- Saving records
- Loading old data
- Updating balances
- Maintaining history

---

### Banking Logic

Challenges:

- Transfer synchronization
- Maintaining state
- Account lifecycle handling
- History consistency

---

## 💡 Solutions Applied

✅ Separated project responsibilities

```bash
account.py → Account operations

bank.py → Banking logic

main.py → Entry point
```

✅ Implemented modular architecture

✅ Added persistent JSON storage

✅ Used OOP design

✅ Organized project structure

---

## 🔮 Future Improvements

- GUI version using Tkinter
- SQLite database support
- Password encryption
- Admin dashboard
- Search functionality
- Email notifications
- Transaction receipts
- Web application version
- API integration
- Multi-user support

---

## ✨ Key Highlights

🏦 Banking management system

💸 Money transfer feature

📜 Transaction history tracking

⚠ Account lifecycle control

💾 Persistent JSON storage

🧠 OOP implementation

📂 Structured project architecture

🚀 Modular Python project

---

## 🤝 Contributing

Contributions are welcome.

Feel free to:

⭐ Star the repository

🍴 Fork the project

📢 Share feedback

🚀 Submit pull requests

---

## ⭐ Support

If you like this project:

⭐ Star this repository

🍴 Fork it

📢 Share it

---

## 👨‍💻 Author

**Saachin Kunwar**

<p align="center">
Built with ❤️ while learning Python architecture, OOP, and software design
</p>

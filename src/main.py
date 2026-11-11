import cmath
import time

import cs50 as cs
import numpy as np
import pandas as pd

company = "MITTI"
admins = [
    {"name": "Brandon", "email": "brandon@gmail.com", "password": "brandon123"},
    {"name": "jajyuu", "email": "jajyuu@gmail.com", "password": "jajyuu123"},
]
users = {
    "arjun@gmail.com": {
        "name": "Arjun",
        "email": "arjun@gmail.com",
        "password": "arjun123",
        "age": 25,
    },
    "john@gmail.com": {
        "name": "John",
        "email": "john@gmail.com",
        "password": "john123",
        "age": 30,
    },
    "mittens@gmail.com": {
        "name": "Mittens",
        "email": "mittens@gmail.com",
        "password": "mittens123",
        "age": 22,
    },
}


def create_user():
    name = cs.get_string("Enter your name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return

    age = cs.get_int("Enter your age: ")
    if age is None:
        return
    if age < 18:
        print("You are not eligible to create an account.")
        return
    if age > 75:
        print("You are too old to create an account.")
        return

    email = cs.get_string("Enter your email: ").strip().lower()
    if not email or "@" not in email or "." not in email.split("@")[-1]:
        print("Please enter a valid email address.")
        return
    if email in users:
        print("This email has already been used.")
        return

    password = cs.get_string("Enter your password: ").strip()
    if len(password) < 6 or len(password) > 20:
        print("Password must be between 6 and 20 characters.")
        return
    if not any(char.isalpha() for char in password) or not any(
        char.isdigit() for char in password
    ):
        print("Password must contain both letters and numbers.")
        return

    users[email] = {
        "name": name,
        "age": age,
        "email": email,
        "password": password,
    }
    print(f"Account created successfully for {name}.")


def login():
    email = cs.get_string("Enter your email: ").strip().lower()
    password = cs.get_string("Enter your password: ").strip()

    user = users.get(email)
    if user is not None and user["password"] == password:
        print(f"Welcome back, {user['name']}!")
    else:
        print("Invalid email or password.")


def display_users():
    if not users:
        print("No users found.")
        return

    rows = [
        {"Name": user["name"], "Age": user["age"], "Email": user["email"]}
        for user in users.values()
    ]
    print("\nRegistered users:")
    print(pd.DataFrame(rows).to_string(index=False))


def admin_menu(admin_user):
    while True:
        print(f"\nADMIN MENU — {admin_user['name']}")
        print("1. Display registered users")
        print("2. Log out")

        choice = cs.get_string("Choose an option (1-2): ").strip()
        if choice == "1":
            display_users()
        elif choice == "2":
            print("Admin logged out.")
            return
        else:
            print("Invalid choice. Enter 1 or 2.")


def admin_login():
    email = cs.get_string("Enter the admin's email: ").strip().lower()
    password = cs.get_string("Enter the admin's password: ").strip()

    for admin_user in admins:
        if admin_user["email"].lower() == email and admin_user["password"] == password:
            print(f"Admin login successful. Welcome, {admin_user['name']}!")
            admin_menu(admin_user)
            return

    print("Invalid admin credentials.")


def main():
    while True:
        print(f"\nWELCOME TO {company}")
        print("1. Create Account")
        print("2. Login")
        print("3. Quit")
        print("4. Admin Login")

        choice = cs.get_string("Enter your choice (1-4): ").strip()

        if choice == "1":
            create_user()
        elif choice == "2":
            login()
        elif choice == "3":
            print(f"Thank you for using {company}. Goodbye!")
            break
        elif choice == "4":
            admin_login()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()

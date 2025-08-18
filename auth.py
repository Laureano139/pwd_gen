import bcrypt
import json
import os
from pwd_gen import *
from applogs import log_event

USERS_FILE = "./users/users.json"
ACCOUNTS_DIR = "./accounts"

def ensure_storage():
    os.makedirs(os.path.dirname(USERS_FILE), exist_ok=True)
    os.makedirs(ACCOUNTS_DIR, exist_ok=True)
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'w') as f:
            json.dump({}, f, indent=4)

ensure_storage()

def load_users():
    try:
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_users(users_data):
    with open(USERS_FILE, 'w') as f:
        json.dump(users_data, f, indent=4)

def register_user():
    print("\n--- Register new user ---")
    users = load_users()
    
    while True:
        username = input("Choose a username: ").strip().lower()
        if not username:
            print("Username cannot be empty.")
        elif username in users:
            print("This username already exists. Please choose another.")
        else:
            break

    while True:
        password = input("Define your master password (at least 8 characters): ")
        if len(password) < 8:
            print("Password must be at least 8 characters long.")
            continue
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            accounts_file = f"{username}_accounts.json"
            
            users[username] = {
                "password_hash": hashed_password,
                "accounts_file": os.path.join(ACCOUNTS_DIR, accounts_file)
            }
            save_users(users)
            
            if not os.path.exists(ACCOUNTS_DIR):
                os.makedirs(ACCOUNTS_DIR)
            
            with open(os.path.join(ACCOUNTS_DIR, accounts_file), 'w') as f:
                json.dump([], f, indent=4)

            print(f"User '{username}' registered successfully!")
            log_event("user_registered", user=username)
            return True
        else:
            print("Passwords do not match. Please try again.")

def login_user():
    print("\n--- Login ---")
    users = load_users()
    
    if not users:
        print("No users registered yet.")
        return False, None

    username = input("Username: ").strip().lower()
    password = input("Password: ")

    user_data = users.get(username)
    
    if user_data:
        hashed_password = user_data["password_hash"].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            print(f"Login successful! Welcome, {username}!")
            log_event("login_success", user=username)
            return True, user_data
        else:
            print("Incorrect password.")
            log_event("login_failure", user=username)

    else:
        print("Error: User not found!")
        log_event("login_unknown_user", user=username)
    
    return False, None

def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            success, user_data = login_user()
            if success:
                print(f"\nYour accounts file is: {user_data['accounts_file']}")
                main(user_data['accounts_file'])
                return True, user_data
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Exiting...")
            log_event("app_exit")
            return False, None
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    is_authenticated, user_info = main_menu()
    if is_authenticated:
        pass

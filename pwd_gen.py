import os, random, string, json

#TODO -> Encrypt json file and passwords

def main():
    print("Welcome to the Password Generator!\n")
    print("1 - Generate a new password")
    print("2 - Retrieve an existing password")
    print("3 - Change email/password")
    print("4 - Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()
    if choice == "1":
        add_new_acc()
    elif choice == "2":
        retrieve_password()
    elif choice == "3":
        change_email_password()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice. Please try again.")
        main()

def add_new_acc():
    platform = input("Enter the platform name: ").strip()
    with open("./accounts/accounts.json", "r") as f:
        if os.path.getsize("./accounts/accounts.json") == 0:
                accs_json = []
        else:
            accs_json = json.load(f)
    for i in accs_json:
        if os.path.getsize("./accounts/accounts.json") == 0:
            continue
        elif i["Platform"].lower() == platform.lower():
            print("Existing account found! Choose one option: \n")
            print("1 - Show the existing password")
            print("2 - Generate a new password and update")
            print("3 - Cancel")
            choice = input("Enter your choice (1/2/3): ").strip()
            if choice == "1":
                print("Existing password: ", i["Password"])
                break
            elif choice == "2":
                new_pwd = gen_pwd()
                print("New password generated: ", new_pwd)
                i["Password"] = new_pwd
                with open("./accounts/accounts.json", "w") as f:
                    json.dump(accs_json, f, indent=4)
            elif choice == "3":
                break
            break
    else:
        generated_password = gen_pwd()
        print("Would you want to associate an email with this account? (yes/no): \n")
        email_association = input().strip().lower()
        if email_association == "yes" or email_association == "y":
            email = input("Enter the email address: ").strip()
        else:
            email = None
        account = {
            "Platform": platform,
            "Email": email,
            "Password": generated_password
        }

        os.makedirs("./accounts", exist_ok=True)

        try:
            with open("./accounts/accounts.json", "r") as f:
                accounts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            accounts = []

        accounts.append(account)

        with open("./accounts/accounts.json", "w") as f:
            json.dump(accounts, f, indent=4)

def gen_pwd():
    pwd_length = 12
    pwd = ''

    pwd_characters = string.ascii_letters + string.digits + string.punctuation

    min_req = (
        random.choice(string.ascii_letters.upper()) 
        + random.choice(string.ascii_letters.lower()) 
        + random.choice(string.digits) 
        + random.choice(string.punctuation)
    )

    # print(min_req)

    password = pwd + min_req + ''.join(random.choice(pwd_characters) for i in range(pwd_length - 4))

    # print("Fst password: ", password)

    mixed_pwd = ''.join(random.sample(password, k=12))

    print("Generated Password: ", mixed_pwd)
        
    return mixed_pwd

def retrieve_password():
    with open("./accounts/accounts.json", "r") as f:
        existing_accounts = json.load(f)
    print("Choose one of the existing accounts:\n")
    c = 1

    for acc in existing_accounts:
        print(f"{c} -> {acc['Platform']}")
        c += 1
        
    input_choice = input("Enter the number of the account you want to retrieve: ").strip()
    if input_choice.isdigit() and 1 <= int(input_choice) < c:
        selected_account = existing_accounts[int(input_choice) - 1]
        print(f"Platform: {selected_account['Platform']}")
        print(f"Email: {selected_account['Email']}")
        print(f"Password: {selected_account['Password']}")
    else:
        print("Invalid choice.")
        
def change_email_password():
    with open("./accounts/accounts.json", "r") as f:
        existing_accounts = json.load(f)
    print("Choose one of the existing accounts:\n")
    c = 1

    for acc in existing_accounts:
        print(f"{c} -> {acc['Platform']}")
        c += 1

    input_choice = input("Enter the number of the account you want to change: ").strip()
    if input_choice.isdigit() and 1 <= int(input_choice) < c:
        selected_account = existing_accounts[int(input_choice) - 1]
        print(f"Platform: {selected_account['Platform']}")
        print(f"Email: {selected_account['Email']}")
        print(f"Password: {selected_account['Password']}")

        print("What do you want to change?")
        print("1 - Email")
        print("2 - Password")
        change_choice = input("Enter your choice (1/2): ").strip()

        if change_choice == "1":
            new_email = input("Enter the new email address: ").strip()
            if new_email:
                selected_account['Email'] = new_email
        elif change_choice == "2":
            print("Choose the action you want to do:")
            print("1 - Generate a new password")
            print("2 - Enter a password manually")
            password_choice = input("Enter your choice (1/2): ").strip()

            if password_choice == "1":
                new_password = gen_pwd()
            elif password_choice == "2":
                new_password = input("Enter the new password: ").strip()
                if new_password == "":
                    print("Password cannot be empty! Please enter a valid password.")
                    return
            else:
                print("Invalid choice.")
                return

            selected_account['Password'] = new_password

        with open("./accounts/accounts.json", "w") as f:
            json.dump(existing_accounts, f, indent=4)
    else:
        print("Invalid choice.")

if __name__ == "__main__":
    main()
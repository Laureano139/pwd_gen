import os, random, string, json

#TODO -> Encrypt json file and passwords | App menu | Option to get a password from a platform account

def main():
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
            print("1 - Show existing password")
            print("2 - Generate new password")
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
            
def main_menu():
    print("Welcome to the Password Generator!\n")
    print("1 - Generate a new password")
    print("2 - Retrieve an existing password")
    print("3 - Change email/password")
    print("4 - Exit")

    choice = input("Enter your choice (1/2/3/4): ").strip()
    if choice == "1":
        main()
    # elif choice == "2":
    #     retrieve_password()
    # elif choice == "3":
    #     change_email_password()
    # elif choice == "4":
    #     exit()
    else:
        print("Invalid choice. Please try again.")
        main_menu()

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

if __name__ == "__main__":
    main()
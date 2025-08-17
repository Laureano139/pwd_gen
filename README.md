
# Overview

This project is a simple yet functional password manager and generator built in Python.

It allows users to securely register, log in and manage their account credentials (platform, email, and password).

This tool also generates strong random passwords that meet common security requirements, such as the use of special characters, numbers and upper and lowercase letters.

It is designed to help users store, retrieve, and update credentials without relying on external services.


# Features

## User Authentication

- Register new users with a master password, hashed using bcrypt lib;
- Secure login system with password verification;
- Each user has a dedicated JSON file to store their credentials;

## Password Generator

Creates 12-character random passwords with:
- Upper and lowercase letters;
- Numbers;
- Special characters;

This ensures strong and secure passwords, hard to crack.

## Account Management

- Add new accounts with platform, email (optional) and password;
- Retrieve/Check saved credentials;
- Update/Change email or passwords;
- Prevent duplicate entries for the same platform;

## Data Storage

- User data stored in /users/users.json;
- Each user has an account file inside /accounts/;


# Run program

## Clone this repository

`git clone https://github.com/Laureano139/pwd_gen.git`

## Install requirements

`pip install -r requirements`

## Run the main script

`python auth.py`


# Inside the program

This is a simple program, with a simple interface (terminal)

When your run the file "auth.py", it will print a main menu, which you can interact.

```
--- Main Menu ---
1 - Login
2 - Register
3 - Exit
```

First of all, you will need to register, so, pick a username and a password and login right after!

## Register

- Choose the option 2. Register;
- Enter a unique username;
- Set a password (minimum 8 characters);
- Confirm the password;
- A new account file will be created for you;

## Login

- Choose the option 1. Login;
- Enter your username and password;
- On successful login, you will be redirected to the Password Manager Menu;

# Password Manager Menu

When you successfully log in, it will be printed a new menu, the menu of the main application:

```
1 - Generate a new password
2 - Retrieve an existing password
3 - Change email/password
4 - Exit
```

## What can you do now?

EXPLORE!!!

## Generate a new password

- Add a new platform;
- Choose whether to associate an email;
- A strong password will be generated and stored;

## Retrieve a password

- Select one of your stored platform accounts;
- View saved platform, email, and password;

## Change email or password

- Select an account;
- Update either the email or generate a new password or enter a new password manually;

# Future Improvements

## Encrypt account files for better security

## Improve UI/UX with a GUI
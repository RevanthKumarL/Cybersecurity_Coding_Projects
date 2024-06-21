import secrets
import string
import os

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the password generator and authentication system!")
    username = input("Enter your username: ")
    password_option = input("Do you want to generate a random password? (yes/no): ")
    
    if password_option.lower() == "yes":
        password_length = int(input("Enter the desired password length: "))
        password = generate_password(password_length)
        print("Generated password:", password)
    else:
        password = input("Enter your password: ")
    
    print("Your username and password have been saved.")
    print("Now, let's authenticate your credentials.")
    
    entered_username = input("Enter your username: ")
    entered_password = input("Enter your password: ")
    
    if entered_username == username and entered_password == password:
        print("Login successful!")
    else:
        print("Invalid username or password. Try again!")

if __name__ == "__main__":
    main()
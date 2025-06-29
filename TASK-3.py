import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter desired password length: "))
        if length <= 0:
            print("Length must be a positive number.")
            return
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

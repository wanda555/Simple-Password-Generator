import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None

    # Define character sets
    letters = string.ascii_letters  # a-z A-Z
    digits = string.digits          # 0-9
    symbols = string.punctuation    # !@#$%^&* etc.

    # Combine all characters
    all_chars = letters + digits + symbols

    # Generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

# User input
try:
    user_length = int(input("Enter password length: "))
    password = generate_password(user_length)
    if password:
        print(f"Your generated password is: {password}")
except ValueError:
    print("Please enter a valid number.")

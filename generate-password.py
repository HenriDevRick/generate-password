import random
import string

def generate_password(length, include_special_chars=True):
    
    chars = string.ascii_letters  # Include letters by default
    digits = string.digits  # Digits to ensure inclusion
    special_chars = string.punctuation if include_special_chars else ""

    # Ensure the password includes at least one digit
    password = [random.choice(digits)]

    # Fill the rest of the password length
    all_chars = chars + digits + special_chars
    password += [random.choice(all_chars) for _ in range(length - 1)]
    
    # Shuffle to ensure the digit is not always at the beginning
    random.shuffle(password)
    
    return ''.join(password)

length = int(input("Enter the password length: "))
include_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

print("Generated password:", generate_password(length, include_special_chars))

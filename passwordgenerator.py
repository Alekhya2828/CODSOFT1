import random
import string

def generate_password(length):
    # Define the characters to include in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password using the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    try:
        # Ask the user for the desired password length
        length = int(input("Enter the desired length of your password: "))
        
        # Ensure the length is a reasonable number
        if length < 6:
            print("It's recommended to use at least 6 characters for better security.")
            length = int(input("Enter a length of 6 or more: "))
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Your generated password is: {password}")
    
    except ValueError:
        print("Invalid input! Please enter a numeric value for the password length.")

# Run the password generator
main()

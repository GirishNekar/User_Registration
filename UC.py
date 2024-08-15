"""
@Author: Girish
@Date: 2024-08-12
@Last Modified by: Girish
@Last Modified time: 2024-08-12
@Title: Validate User's First Name, Last Name, Email, Mobile Number, and Password
"""

import re

def validate_first_name(first_name: str) -> bool:
    """
    Description: 
        Checks for a valid first name.
    Parameter: 
        first_name (str): The first name to validate.
    Return: 
        bool: True if the first name is valid, False otherwise.
    """
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return bool(re.search(pattern, first_name))


def validate_last_name(last_name: str) -> bool:
    """
    Description: 
        Checks for a valid last name.
    Parameter: 
        last_name (str): The last name to validate.
    Return: 
        bool: True if the last name is valid, False otherwise.
    """
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return bool(re.search(pattern, last_name))


def validate_email(email: str) -> bool:
    """
    Description:
        Validates the email format according to the given criteria.
    Parameter:
        email (str): The email to validate.
    Return:
        bool: True if the email is valid, False otherwise.
    """
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2,3})?$'
    return bool(re.search(pattern, email))


def validate_mobile_number(mobile: str) -> bool:
    """
    Description:
        Validates the mobile number format according to the given criteria.
    Parameter:
        mobile (str): The mobile number to validate.
    Return:
        bool: True if the mobile number is valid, False otherwise.
    """
    pattern = r'^\d{2} \d{10}$'
    return bool(re.search(pattern, mobile))


def validate_password(password: str) -> bool:
    """
    Description:
        Validates the password according to the given criteria using regular expressions.
        The password must be at least 8 characters long, contain at least one uppercase letter,
        include at least one numeric digit, and have exactly one special character.
    Parameter:
        password (str): The password to validate.
    Return:
        bool: True if the password is valid, False otherwise.
    """
    # Rule1: Minimum 8 characters
    # Rule2: At least one uppercase letter
    # Rule3: At least one numeric digit
    # Rule4: Exactly one special character
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`-]).{8,}$'
    
    if not re.search(pattern, password):
        return False
    
    # Ensure exactly one special character
    special_char_count = len(re.findall(r'[!@#$%^&*()_+{}\[\]:;"\'<>,.?/~`-]', password))
    
    return special_char_count == 1


def get_user_input(prompt: str) -> str:
    """
    Description: 
        Gets user input for the provided prompt.
    Parameter: 
        prompt (str): The prompt message to display.
    Return: 
        str: The user input.
    """
    return input(prompt)


def main():
    """
    Description:
        Main function to validate the user's first name, last name, email, mobile number, and password.
    Parameter:
        None
    Return:
        None
    """
    first_name = get_user_input("Enter a valid First Name: ")
    last_name = get_user_input("Enter a valid Last Name: ")
    email = get_user_input("Enter a valid Email: ")
    mobile_number = get_user_input("Enter a valid Mobile Number (e.g., 91 9919819801): ")
    password = get_user_input("Enter a valid Password (minimum 8 characters, at least one uppercase letter, at least one numeric digit, and exactly one special character): ")

    if (validate_first_name(first_name) and 
        validate_last_name(last_name) and 
        validate_email(email) and 
        validate_mobile_number(mobile_number) and 
        validate_password(password)):
        print("Valid Name, Email, Mobile Number, and Password")
    else:
        print("Invalid Name, Email, Mobile Number, or Password")


if __name__ == "__main__":
    main()

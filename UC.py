"""
@Author: Girish
@Date: 2024-08-12
@Last Modified by: Girish
@Last Modified time: 2024-08-12
@Title: Validate User's First Name, Last Name, and Email
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


def get_user_input(prompt: str) -> str:
    """
    Description : 
        Gets user input for the provided prompt.
    Parameter : 
        prompt (str): The prompt message to display.
    Return: 
        str: The user input.
    """
    return input(prompt)


def main():
    """
    Description:
        Main function to validate the user's first name, last name, and email.
    Parameter:
        None
    Return:
        None
    """
    first_name = get_user_input("Enter a valid First Name: ")
    last_name = get_user_input("Enter a valid Last Name: ")
    email = get_user_input("Enter a valid Email: ")

    if validate_first_name(first_name) and validate_last_name(last_name) and validate_email(email):
        print("Valid Name and Email")
    else:
        print("Invalid Name or Email")


if __name__ == "__main__":
    main()

"""
@Author: Girish
@Date: 2024-08-14
@Last Modified by: Girish
@Last Modified time: 2024-08-14
@Title: Check for Users First name and Last name is Valid or not
"""

import re

def validate_first_name(first_name: str) -> bool:
    
    
    """
    Descripton: 
        Checks for the valid name
    param name: 
        The name to validate.
    return: 
        True if the name is valid, False otherwise.
    """
    
    
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return bool(re.search(pattern, first_name))

def validate_last_name(last_name: str) -> bool:
    
    
    """
    Descripton: 
        Checks for the valid name
    param name: 
        The name to validate.
    return: 
        True if the name is valid, False otherwise.
    """
    
    
    pattern = r'^[A-Z][A-Za-z]{2,}$'
    return bool(re.search(pattern, last_name))


def get_user_input() -> str:
    
    
    """
    Description : 
        Gets user input for the name.
    Parameter : 
        None
    return: 
        The name entered by the user.
    """
    
    return input("Enter the valid Name: ")



def main():

    first_name = get_user_input()
    last_name = get_user_input()
    if validate_first_name(first_name) and validate_last_name(last_name):
        print("Valid Name")
    else:
        print("Invalid Name")



if __name__ == "__main__":
    main()

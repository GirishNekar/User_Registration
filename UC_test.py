"""
@Author: Girish
@Date: 2024-08-12
@Last Modified by: Girish
@Last Modified time: 2024-08-12
@Title: Unit tests for validating first name, last name, email, mobile number, and password
"""

import unittest
from UC import (
    validate_first_name,
    validate_last_name,
    validate_email,
    validate_mobile_number,
    validate_password,
)

class TestUserValidation(unittest.TestCase):
    """
    Unit test class for validating the functionality of first name, last name, email, mobile number, and password validation.
    """

    def test_valid_first_name(self):
        """
        Description:
            Tests the validation function for first names.
        Parameters:
            self: Instance of the class.
        Return:
            None
        """
        self.assertTrue(validate_first_name("John"), "Should be valid")
        self.assertTrue(validate_first_name("Alice"), "Should be valid")
        self.assertFalse(validate_first_name("Jo"), "Should be invalid due to length")
        self.assertFalse(validate_first_name("Al"), "Should be invalid due to length")
        self.assertFalse(validate_first_name("john"), "Should be invalid due to lowercase first letter")
        self.assertFalse(validate_first_name("alice"), "Should be invalid due to lowercase first letter")
        self.assertFalse(validate_first_name("Jo@n"), "Should be invalid due to the presence of a special character")
        self.assertFalse(validate_first_name("Al!ce"), "Should be invalid due to the presence of a special character")
        self.assertFalse(validate_first_name("John123"), "Should be invalid due to the presence of a number")
        self.assertFalse(validate_first_name("Alice456"), "Should be invalid due to the presence of a number")

    def test_valid_last_name(self):
        """
        Description:
            Tests the validation function for last names.
        Parameters:
            self: Instance of the class.
        Return:
            None
        """
        self.assertTrue(validate_last_name("Smith"), "Should be valid")
        self.assertTrue(validate_last_name("Johnson"), "Should be valid")
        self.assertFalse(validate_last_name("Sm"), "Should be invalid due to length")
        self.assertFalse(validate_last_name("Jo"), "Should be invalid due to length")
        self.assertFalse(validate_last_name("smith"), "Should be invalid due to lowercase first letter")
        self.assertFalse(validate_last_name("johnson"), "Should be invalid due to lowercase first letter")
        self.assertFalse(validate_last_name("Sm!th"), "Should be invalid due to the presence of a special character")
        self.assertFalse(validate_last_name("Jo@nson"), "Should be invalid due to the presence of a special character")
        self.assertFalse(validate_last_name("Smith123"), "Should be invalid due to the presence of a number")
        self.assertFalse(validate_last_name("Johnson456"), "Should be invalid due to the presence of a number")

    def test_valid_email(self):
        """
        Description:
            Tests the validation function for emails.
        Parameters:
            self: Instance of the class.
        Return:
            None
        """
        self.assertTrue(validate_email("abc.xyz@bl.co.in"), "Should be valid")
        self.assertTrue(validate_email("user@domain.co"), "Should be valid")
        self.assertFalse(validate_email("abc@blco"), "Should be invalid due to missing dot before TLD")
        self.assertFalse(validate_email("abc@bl.co.in."), "Should be invalid due to trailing dot")
        self.assertFalse(validate_email("user@domaincom"), "Should be invalid due to missing dot in domain")
        self.assertFalse(validate_email("@bl.co"), "Should be invalid due to missing user part")
        self.assertFalse(validate_email("user@.com"), "Should be invalid due to missing domain part")
        self.assertFalse(validate_email("user@domain.c"), "Should be invalid due to TLD being too short")
        self.assertFalse(validate_email("user@domain.toolongtld"), "Should be invalid due to TLD being too long")
        self.assertFalse(validate_email("userdomain.com"), "Should be invalid due to missing @ symbol")

    def test_valid_mobile_number(self):
        """
        Description:
            Tests the validation function for mobile numbers.
        Parameters:
            self: Instance of the class.
        Return:
            None
        """
        self.assertTrue(validate_mobile_number("91 9919819801"), "Should be valid")
        self.assertTrue(validate_mobile_number("44 1234567890"), "Should be valid")
        self.assertFalse(validate_mobile_number("919919819801"), "Should be invalid due to missing space")
        self.assertFalse(validate_mobile_number("91 991981980"), "Should be invalid due to insufficient digits")
        self.assertFalse(validate_mobile_number("91 99198198012"), "Should be invalid due to excessive digits")
        self.assertFalse(validate_mobile_number("91-9919819801"), "Should be invalid due to incorrect separator")
        self.assertFalse(validate_mobile_number("9919819801"), "Should be invalid due to missing country code")
        self.assertFalse(validate_mobile_number("91 99198198O1"), "Should be invalid due to non-numeric characters")

    def test_valid_password(self):
        """
        Description:
            Tests the validation function for passwords.
        Parameters:
            self: Instance of the class.
        Return:
            None
        """
        self.assertTrue(validate_password("StrongPass123"), "Should be valid")
        self.assertFalse(validate_password("pass123"), "Should be invalid due to length")



if __name__ == "__main__":
    unittest.main()

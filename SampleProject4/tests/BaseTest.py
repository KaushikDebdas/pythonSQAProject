import datetime
import random
import string

from SampleProject4.utilites.LogFileGenerate import Logger
from faker import Faker

class BaseTest:
    # every time generate new email
    def generate_email_with_timestamp(self, prefix="user", domain="example.com"):
        """
        Generate a new email address with a timestamp appended to it.
        Args:
            prefix (str): The prefix part of the email address. Default is "user".
            domain (str): The domain part of the email address. Default is "example.com".
        Returns:
            str: The generated email address with timestamp.
        """
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        email = f"{prefix}_{timestamp}@{domain}"
        return email

    # every time generate new password
    def generate_random_password(self, length=12):
        """
        Generate a random password.
        Args:
            length (int): Length of the password. Default is 12.
        Returns:
            str: The generated random password.
        """
        # Define the characters to use for the password
        characters = string.ascii_letters + string.digits + string.punctuation
        # Generate the password
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

    # every time generate random bd mobile number
    def generate_bd_mobile_number(self):
        """
        Generate a random Bangladeshi mobile number with country code +880.
        Returns:
            str: The generated mobile number.
        """
        # Bangladeshi mobile numbers have a fixed length of 11 digits
        mobile_number = "+880"
        for _ in range(8):
            mobile_number += str(random.randint(0, 9))
        return mobile_number
    # Generate and print a random Bangladeshi mobile number

    def fake_name_genarator(self):
        fake = Faker()
        random_first_name = fake.first_name()
        random_last_name = fake.last_name()

        return random_first_name, random_last_name

    # Logger reuse from LogFileGenerate.py file
    def log_info(self, msg):
        Logger.info(msg)

    def log_update(self, msg):
        Logger.update(msg)

    def log_exception(self, msg):
        Logger.exception(msg)

    def log_debug(self, msg):
        Logger.debug(msg)

    def log_object(self, object):
        Logger.object(object)

    def log_clear(self):
        Logger.clear()
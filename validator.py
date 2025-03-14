import re
from datetime import datetime
from urllib.parse import urlparse

class DataValidator:
    """
    This class helps check if personal data, like emails, phone numbers, dates, and URLs, are correctly formatted.
    """
    def __init__(self, data):
        """
        Sets up the class with the data to be checked.
        :param data: The piece of information to validate.
        """
        self.data = data

    def validate_email(self):
        """
        Checks if the given data looks like a valid email address.
        :return: True if it's a valid email, False otherwise.
        """
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return bool(re.match(pattern, self.data))

    def validate_phone(self):
        """
        Checks if the given data looks like a valid phone number.
        It supports different formats, including international ones.
        :return: True if it's a valid phone number, False otherwise.
        """
        pattern = r'^\+?[0-9]{1,3}?[-.\s]?\(?[0-9]{1,4}?\)?[-.\s]?[0-9]{1,4}[-.\s]?[0-9]{1,9}$'
        return bool(re.match(pattern, self.data))

    def validate_date(self, date_format="%Y-%m-%d"):
        """
        Checks if the given data is a correctly formatted date.
        :param date_format: The expected format of the date (default is "YYYY-MM-DD").
        :return: True if it's a valid date, False otherwise.
        """
        try:
            datetime.strptime(self.data, date_format)
            return True
        except ValueError:
            return False

    def validate_url(self):
        """
        Checks if the given data is a valid URL.
        It ensures the URL has a proper structure, like starting with 'http' or 'https'.
        :return: True if it's a valid URL, False otherwise.
        """
        try:
            result = urlparse(self.data)
            return all([result.scheme, result.netloc])
        except:
            return False

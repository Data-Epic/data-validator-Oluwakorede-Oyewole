import unittest
from validator import DataValidator


class TestDataValidator(unittest.TestCase):

    def test_validate_email(self):
        self.assertTrue(DataValidator("test@example.com").validate_email())
        self.assertTrue(DataValidator("user.name+tag@domain.co.uk").validate_email())
        self.assertFalse(DataValidator("invalid-email").validate_email())
        self.assertFalse(DataValidator("user@.com").validate_email())

    def test_validate_phone(self):
        self.assertTrue(DataValidator("+1234567890").validate_phone())
        self.assertTrue(DataValidator("(123) 456-7890").validate_phone())
        self.assertFalse(DataValidator("123-abc-7890").validate_phone())
        self.assertFalse(DataValidator("+1 (234").validate_phone())

    def test_validate_date(self):
        self.assertTrue(DataValidator("2023-12-31").validate_date())
        self.assertTrue(DataValidator("31/12/2023").validate_date("%d/%m/%Y"))
        self.assertFalse(DataValidator("31-12-2023").validate_date())
        self.assertFalse(DataValidator("invalid-date").validate_date())

    def test_validate_url(self):
        self.assertTrue(DataValidator("https://www.example.com").validate_url())
        self.assertTrue(DataValidator("http://example.org").validate_url())
        self.assertFalse(DataValidator("www.example").validate_url())
        self.assertFalse(DataValidator("example").validate_url())


if __name__ == "__main__":
    unittest.main()

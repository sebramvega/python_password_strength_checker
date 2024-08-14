import unittest
from password_checker import check_password_strength


class TestPasswordStrengthChecker(unittest.TestCase):

    def test_strong_password(self):
        self.assertEqual(check_password_strength("Str0ng!Pass"), "strong")

    def test_medium_password(self):
        self.assertEqual(check_password_strength("Medium1Pass"), "medium")

    def test_weak_password(self):
        self.assertEqual(check_password_strength("weakpass"), "weak")

    def test_short_password(self):
        self.assertEqual(check_password_strength("S1!"), "weak")

    def test_no_special_character(self):
        self.assertEqual(check_password_strength("StrongPass1"), "medium")


if __name__ == "__main__":
    unittest.main()

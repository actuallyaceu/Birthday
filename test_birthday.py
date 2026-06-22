import unittest
from datetime import date

from birthday import calculate_age, get_weekday, is_leap_year, render_date


class BirthdayTest(unittest.TestCase):
    def test_weekday(self):
        self.assertEqual(get_weekday(date(2000, 1, 1)), "суббота")

    def test_leap_year(self):
        self.assertTrue(is_leap_year(2000))
        self.assertTrue(is_leap_year(2024))
        self.assertFalse(is_leap_year(1900))
        self.assertFalse(is_leap_year(2023))

    def test_age_after_birthday(self):
        self.assertEqual(calculate_age(date(2000, 6, 10), date(2026, 6, 23)), 26)

    def test_age_before_birthday(self):
        self.assertEqual(calculate_age(date(2000, 12, 10), date(2026, 6, 23)), 25)

    def test_render_date_has_five_rows(self):
        result = render_date(date(2001, 2, 3))
        self.assertEqual(len(result.splitlines()), 5)
        self.assertNotIn("0", result)
        self.assertNotIn("1", result)


if __name__ == "__main__":
    unittest.main()

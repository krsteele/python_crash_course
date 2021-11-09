# Exercise 11-1: City, Country
import unittest
from city_functions import city_country_name


class CitiiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Does input like 'santiago' and 'chile' work?"""
        formatted_city = city_country_name('santiago', 'chile')

        self.assertEqual(formatted_city, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
# Exercise 11-1: City, Country and 11-2: Population
import unittest
from city_functions import city_country_name


class CitiiesTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country(self):
        """Does input like 'santiago' and 'chile' work?"""
        formatted_city = city_country_name('santiago', 'chile')

        self.assertEqual(formatted_city, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does input like 'santiago', 'chile', '5000000' work?"""
        formatted = city_country_name('santiago', 'chile', '5000000')

        self.assertEqual(formatted, 'Santiago, Chile - Population: 5000000')


if __name__ == '__main__':
    unittest.main()
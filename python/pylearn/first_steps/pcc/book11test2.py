#! Занятие по книге Python Crash Course, chapter 11, "Testing your
# Code".  Занятие первое, тесты.
import unittest
from book11functions import get_formatted_name, city_functions
# Тест должен содержать функцию (или импортировать функцию без лишних
# прицепов.


# Тест должен бать наследованным от unittest.TestCase.
class NamesTestCase(unittest.TestCase):
    """Test's for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like Janis Joplin work?"""
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

    def test_city_country_format(self):
        formatted_city = city_functions('santiago', 'chile')
        self.assertEqual(formatted_city, 'Santiago, Chile.')

    def test_city_country_population_format(self):
        formatted_city = city_functions('santiago', 'chile', 5000000)
        self.assertEqual(formatted_city,
                         'Santiago, Chile - population 5000000.')


unittest.main()
# Запускает тесты в файле.

# Точка обозначает, что пройден один тест.

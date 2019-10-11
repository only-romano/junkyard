#! Занятие по книге Python Crash Course, chapter 11, "Testing your
# Code".  Занятие второе, тесты.
import unittest
from book11classes import AnonymousSurvey, Employee


class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey."""

    # Метод setUp позовляет установить значения для всех последующих
    # методов.
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test
        methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['Sexy', 'Girls', 'Dicks']

    def test_store_single_response(self):
        """Test that a single response is srored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


class TestEmployee(unittest.TestCase):
    """Tesrs for the class Employee."""

    def setUp(self):
        name = 'Chicka'
        surname = 'Boom'
        salary = 33000
        self.name = Employee(name, surname, salary)

    def test_give_default_raise(self):
        self.name.give_raise()
        self.assertEqual(self.name.salary, 38000)

    def test_give_custom_raise(self):
        self.name.give_raise(7000)
        self.assertEqual(self.name.salary, 40000)


unittest.main()

#! Занятие по книге Python Crash Course, chapter 11, "Testing your
# Code".  Занятие второе, классы.


class AnonymousSurvey:
    """Collect anonymous answers to a survey question."""

    def __init__(self, question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []

    def show_question(self):
        """Show the survey question."""
        print(self.question)

    def store_response(self, new_response):
        """Store a single response to the survey."""
        self.responses.append(new_response)

    def show_result(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print('- ' + response)


class Employee:
    """Try it yourself 11-3."""

    def __init__(self, first_name, last_name, annual_salary):
        """Store name, surname and annual salary."""
        self.name = first_name
        self.surname = last_name
        self.salary = annual_salary

    def give_raise(self, salary_raise=5000):
        self.salary += salary_raise

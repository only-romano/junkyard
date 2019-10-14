#! Занятие по книге Python Crash Course, chapter 11, "Testing your
# Code".  Занятие второе, код.

# Asserts Methods Available from the unittest Module:
#  ..  assertEqual(a, b) : подтверждает a == b;
#  ..  assertNotEqual(a, b) : подтверждает a != b;
#  ..  assertTrue(a) : подтверждает a is True;
#  ..  assertFalse(a) : подтверждает a is False;
#  ..  assertIn(item, list) : подтверждает что item в list;
#  ..  assertNotIn(item, list) : подтверждает что item не в list.

from book11classes import AnonymousSurvey

question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

print("\nThank you to everyone who participated in the survey!")
my_survey.show_result()

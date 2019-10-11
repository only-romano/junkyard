#! Examples of using cases

names = ['kato basiro', 'albert einstein']

message_1 = 'Hello, {}, would you like to learn some Python today?'
message_2 = '''
{} once said: \n\t"A person who never made a
\t mistake never tried anything new."
'''

print(message_1.format(names[0].title()))
print(message_2.format(names[1].title()))

names[0] = ' kato basiro '

message_3 = '\n{}is too pretty!'
message_4 = '{} is obvious the best.'

print(message_3.format(names[0].lower().lstrip()))
print(message_4.format(names[0].upper().strip()))

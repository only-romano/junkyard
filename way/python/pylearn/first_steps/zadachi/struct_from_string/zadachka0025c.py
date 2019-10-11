#! Штука, которая из такой строчки делает такую структуру


def quote_to_json(x, y, c):
    ...


    # elif x.split()[0] == '>' and x.split[1] == '<':
      #  return quote_to_json(' '.join(x.split()[1:]))
#    x.split().index('>')
 #   while len(x.split()) != 3:
  #      return {'text': x.split()[1], 'children':
   #             quote_to_json(' '.join(x.split()[:]))}
   # return []

file = '../quote_to_json2.json'

with open(file) as file_obj:
    s = file_obj.read()


print(quote_to_json(s, {}, 0))
print(s.split()[0])

#print(quote_to_json(s))

#! Штука, которая из такой строчки делает такую структуру


def quote_to_json(x, y, c, d, e):
    if x[0] == '<' and x[2] == '<':
        c += 2
        y = {'text': x[1], 'children': [quote_to_json(x[2:], y, c, d, e)]}
        if len(x) == e:
            return y
        quote_to_json(x[c+4:], y, 0, d, e)
        return y
    elif x[0] == '<' and x[2] == '>':
        try:
            if y['children']:
                y['children'].append({'text': x[1], 'children': []})
                return y
        except:
            d = {'text': x[1], 'children': []}
            return d
    elif x[0] == '>' and len(x) > 1:
        quote_to_json(x[1:], y, 0, d, e)
    if x[0] == '>' and len(x) == 1:
        return y
    if x.count('<') == 0:
        return y


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


print(quote_to_json(s.split(), {}, 0, [], len(s.split())))
print(s.split()[0])

#print(quote_to_json(s))

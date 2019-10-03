#! Штука, которая из такой строчки делает такую структуру

file = '../quote_to_json2.json'

with open(file) as file_obj:
    s = file_obj.read()
s = s.replace('<', '{').replace('>', '}]').split()
s[-1] = '}'
i = 0
while i < len(s):
    if s[i] == '}]':
        if s[i+1] == '{':
            s[i] = '},'
    if s[i] not in ['{','}', '}]', '},']:
        if s[i+1] == '}]':
            s[i] = '"text": "' + s[i] + '", "children": []'
        else:
            s[i] = '"text": "' + s[i] + '", "children": ['
    i +=1

x = 'z = ' + ''.join(s)
exec(x)

print(z)

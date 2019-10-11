import re

line = 'Cats are smarter than dogs'

match = re.match(r'dogs', line, re.M|re.I)
if match:
  print (match.group())
else:
  print ('No match!')

search = re.search(r'dogs', line, re.M|re.I)
if search:
  print (search.group())


phone = "2004-959-559 # This is Phone Number"

num = re.sub(r'#.*$', '', phone)
print("Phone Num:", num)

num = re.sub(r'\D', "", phone)
print ("Phone Num:", num)

print(r'[Pp]ython')
import re

phoneRegex = re.compile(r'(\d\d\d-\d\d\d-\d\d\d\d)')

mo = phoneRegex.search('my number is 415-555-4242, you number is 423-333-3333')

print(mo.groups())
print(mo.groups())
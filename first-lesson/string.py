import re

string = 'hello python world'

match = re.match('hello[\t]*(.*)world]', string)

print(match.groups())

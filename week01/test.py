import re

pattern = re.compile('[-0-9]+')
x = pattern.match("2020-08-15日本上映")
print(x.group(0))
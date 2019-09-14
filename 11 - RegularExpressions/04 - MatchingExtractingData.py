import re
x = 'My 2 favourite numbers are 19 and 42'
y = re.findall('[0-9]+', x)
print(y)
# (2, 19, 42)

x = 'From lukaszgo@gmail.com Sat Jan'
y = re.findall('\S+@\S+', x)
# lukaszgo@gmail.com

y = re.findall('^From \S+@\S+', x)
# lukaszgo@gmail.com
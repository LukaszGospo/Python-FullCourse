data = 'From lukaszgo@gmail.com Sat Jan'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ',atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

import re
y = re.findall('^From .*@([^ ]*)', data)
print(y)
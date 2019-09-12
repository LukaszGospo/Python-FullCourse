count = 0
try:
    fhand = open('mbox.txt')
except:
    print('File cannot be opened')
    quit()
for line in fhand:
    if line.startswith('From:'):
        print(line)
    print(line.rstrip())
    count += 1
print('Line count: ', count)
# .read() - Whole file in one line
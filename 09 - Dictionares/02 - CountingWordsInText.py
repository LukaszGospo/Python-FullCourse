handle = open('text')

counts = dict()
for line in handle:
    words = line.split()

#print('Words: ', words)

#print('Counting...')
for word in words:
    counts[word] = counts.get(word,0) + 1
#print(counts)

for key in counts:
    print(key, counts[key])

bigword = None
bigcount = None

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = coun t
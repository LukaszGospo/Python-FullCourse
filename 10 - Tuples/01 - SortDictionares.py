hand = open('text')

di = dict()
for lin in hand:
    lin = lin.rstrip()
    wds = lin.split()
    for w in wds:
        # idiom
        di[w] = di.get(w, 0) + 1


x = sorted(di.items())

tmp = list()
for k, v in di.items():
    newt = (v, k)
    tmp.append(newt)

print(sorted(tmp, reverse=True))

for v, k in tmp[:5]:
    print(k, v)
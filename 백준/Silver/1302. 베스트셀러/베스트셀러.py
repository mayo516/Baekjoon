d = dict()

for _ in range(int(input())):
    book = input()
    if book in d:
        d[book] += 1
    else:
        d[book] = 1

maxNum = max(d.values())
candi = []
for k, v in d.items():
    if v == maxNum:
        candi.append(k)

# print(sorted(candi)[0])
candi.sort()
print(candi[0])
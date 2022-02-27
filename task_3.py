users = dict()
us = []
with open('users.csv', 'r', encoding='utf-8') as f:
    for line in f:
        us.append(' '.join(line.split(','))[:-1])
hob = []
with open('hobby.csv', 'r', encoding='utf-8') as f:
    for line in f:
        for el in line.split(','):
            hob.append(el)
if len(us) < len(hob):
    for i in range(len(us)):
        users[us[i]] = hob[i]
    print(users)
    print(1)
else:
    hob += (len(us) - len(hob)) * [None]
    for i in range(len(us)):
        users[us[i]] = hob[i]
    print(users)

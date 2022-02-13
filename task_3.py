# "Иван", "Мария", "Петр", "Илья"
# Иван Мария Петр Илья
def thesaurus(names):
    d = {}
    first_letter = []
    used = [False] * len(names)
    for el in names:
        first_letter.append(el[0])
    for ind,el in enumerate(names):
        if not used[ind]:
            used[ind] = True
            s = [first_letter[ind]]
            for i in range(len(first_letter)):
                if first_letter[i] == el[0]:
                    used[i] = True
                    s.append(names[i])
            d[s[0]] = s[1:]
    print(d)
name = input()
thesaurus(name.split())
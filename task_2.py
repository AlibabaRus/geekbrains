ip = dict()
file_1 = open('nginx_logs.txt', 'r', encoding='utf-8')
for line in file_1:
    k = line.split()[0]
    ip[k] = ip.get(k, 0) + 1
file_1.close()
max_num = 0
ans = ''
for el in ip.keys():
    if ip[el] > max_num:
        max_num = ip[el]
        ans = el
print(ans, max_num)

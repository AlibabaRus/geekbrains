mas = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
ind_list = []
for ind,el in enumerate(mas):
    if el.isdigit():
        mas[ind] = f'{int(el):02d}'
        ind_list.append(ind)
    elif el[1:].isdigit():
        mas[ind] = el[0] + f'{int(el):02d}'
        ind_list.append(ind)        
for ind,el in enumerate(mas):
    if ind in ind_list:
        print("\"" + el + "\"", end=" ")
    else:
        print(el, end=" ")
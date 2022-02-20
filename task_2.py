import requests


def currency_rates(val):
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    content = response.content.decode(encoding=response.encoding)

    сhar_сode = []
    for el in content.split('<CharCode>')[1:]:
        сhar_сode.append(el.split('<')[0])

    nominal = []
    for el in content.split('<Nominal>')[1:]:
        nominal.append(el.split('<')[0])

    value = []
    for el in content.split('<Value>')[1:]:
        value.append(el.split('<')[0])

    ind_val = сhar_сode.index(val)
    st = len(value[ind_val]) - value[ind_val].index(',') - 1
    val_float = int(value[ind_val][:value[ind_val].index(',')] + value[ind_val][value[ind_val].index(',') + 1:])
    price = val_float / int(nominal[ind_val]) / 10 ** st

    return price


print(currency_rates(input()))
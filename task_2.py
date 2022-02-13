def num_translate_adv(number):
    d = {"один" : "one", "два" : "two", "три" : "three", "четыре" : "four", "пять" : "five", 
         "шесть" : "six", "семь" : "seven", "восемь" : "eight", "девять" : "nine", "десять" : "ten"}
    if number.islower():
        print(d[number])
    else:
        print(d[number.lower()].capitalize())    
num = input()
num_translate_adv(num)

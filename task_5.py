import random
def get_jokes(n):
    ans = []
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    used_1 = [False]  * 5
    used_2 = [False]  * 5
    used_3 = [False]  * 5
    for i in range(n):
        ans_1 = random.choice(nouns)
        while used_1[nouns.index(ans_1)]:
            ans_1 = random.choice(nouns)
        used_1[nouns.index(ans_1)] = True
        
        ans_2 = random.choice(adverbs)
        while used_1[adverbs.index(ans_2)]:
            ans_2 = random.choice(adverbs)
        used_2[adverbs.index(ans_2)] = True
        
        ans_3 = random.choice(adjectives)
        while used_3[adjectives.index(ans_3)]:
            ans_3 = random.choice(adjectives)
        used_3[adjectives.index(ans_3)] = True       
        
        ans.append(f'{ans_1} {ans_2} {ans_3}')
    print(ans)
        
get_jokes(int(input()))
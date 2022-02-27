string = input()
nums = string.split()
if len(nums) == 0:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
elif len(nums) == 1:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        f.seek(int(nums[0]) - 1)
        for line in f:
            print(line)
else:
    with open('bakery.csv', 'r', encoding='utf-8') as f:
        f.seek(int(nums[0]) - 1)
        print(f.read(int(nums[1])))

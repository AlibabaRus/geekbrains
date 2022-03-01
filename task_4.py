import os


sizes = {}
for root, dirs, files in os.walk('./'):
    for file in files:
        _size = os.stat(os.path.join(root,file)).st_size
        sizes[10 ** (len(str(_size)))] = sizes.get(10 ** (len(str(_size))), 0) + 1
print(sizes)
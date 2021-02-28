import random

def values():
    f = open('numbers.csv', 'w+')
    for i in range(99):
        f.write(str(random.randint(1, 100)) + ',')
    f.write(str(random.randint(1, 100)))
    f.close()

values()
input('Файл создан.')

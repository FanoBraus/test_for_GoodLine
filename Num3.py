a = int(input('Введите число от 1 до 10:'))
if a < 1 or a > 10:
    print('Error')
    exit()
n = int(input('Введите степень от 0 до 9:'))
if n < 0 or n > 9:
    print('Error')
    exit()
    


def recursive_function(a, n):
    if n == 0:
        return 1
    if n > 0:
        return a * recursive_function(a, n-1)
    return 1

print('Число', a,'в степени', n,'будет равно:', recursive_function(a, n))
input()

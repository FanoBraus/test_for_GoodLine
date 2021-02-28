def sort():
    f = open('numbers.csv', 'r')
    out_file = f.read()
    f.close()
    #print(out_file)
    string_numbers = out_file.split(',')
    #print(string_numbers)
    values = list()

    
    for number in string_numbers:
        values.append(int(number))
    #print(values)
    N = 100
    a = values
    for i in range(N-1):
        for j in range(N-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print('Отсортированные числа пузырьковым методом: ', a)

#Или воспользоваться встроенной функцией Python:

    #values.sort()
    #print('Отсортированные числа: ',values)
    
sort()
input()

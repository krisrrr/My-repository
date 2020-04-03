print('Эта программа получает на вход матрицу любого размера')
print('(в т. ч. число, строку, столбец) и выводит матрицу, ')
print('того же размера, у которой каждый элемент в позиции i, j равен')
print('сумме элементов первой матрицы на позициях (i-1, j), (i+1, j),' )
print('(i, j-1), (i, j+1). У крайних символов соседний элемент находится ')
print('с противоположной стороны матрицы.\n')
lst, k = [], []               # генерация списка для матрицы, первичного списка ввода
print('Введите матрицу построчно, элементы в строке разделяются одним пробелом,')
print('чтобы перейти на следующую строку, нажмите Enter, ')
print('чтобы закончить ввод перейдите на следующую строку и введите end...', end=' ')
while True:                                             
    k = [i for i in input().split()]  # ввод строки в первичный список
    if 'end' in k: break              # обработка окончания ввода
    else: 
        lst.append([])                # добавляем пустую строку в матрицу 
        j += 1
        for i in range(len(k)):
            if k[i] != 'end':
                lst[j - 1].append(int(k[i]))          # добавляем строку из первичного списка в матрицу
if len(lst[0]) == 1 and len(lst) == 1:          # обработка случая, когда подаётся одно число
    print(lst[0][0] * 4)
else:
    lst_sqr = [[] for i in range(len(lst))]     #генерация списка сумм
    if len(lst) != 1 and len(lst[0]) != 1:      # обработка случая матрицы с размерами >1
        for i in range(len(lst)):
            for j in range(len(lst[i])):
                if j != len(lst[i]) - 1 and i != len(lst) - 1:
                    lst_sqr[i].append(lst[i - 1][j] + lst[i + 1][j] + lst[i][j - 1] + lst[i][j + 1])
                else:
                    if j == len(lst[i]) - 1 and i == len(lst) - 1:
                        lst_sqr[i].append(lst[i - 1][j] + lst[0][j] + lst[i][j - 1] + lst[i][0])
                    elif i == len(lst) - 1:
                        lst_sqr[i].append(lst[i - 1][j] + lst[0][j] + lst[i][j - 1] + lst[i][j + 1])
                    elif j == len(lst[i]) - 1:
                        lst_sqr[i].append(lst[i - 1][j] + lst[i + 1][j] + lst[i][j - 1] + lst[i][0])
    elif len(lst) == 1 and len(lst[0]) != 1:    # обработка строки
        for j in range(len(lst[0])):
            if j != len(lst[0]) - 1:
                lst_sqr[0].append(lst[0][j] + lst[0][j] + lst[0][j - 1] + lst[0][j + 1])
            else: lst_sqr[0].append(lst[0][j] + lst[0][j] + lst[0][j - 1] + lst[0][0])
    elif len(lst) != 1 and len(lst[0]) == 1:    # обработка столбца
        for i in range(len(lst)):
            if i != len(lst) - 1:
                lst_sqr[i].append(lst[i][0] + lst[i][0] + lst[i + 1][0] + lst[i - 1][0])
            else:  lst_sqr[i].append(lst[i][0] + lst[i][0] + lst[0][0] + lst[i - 1][0])    
    for i in range(len(lst_sqr)):
        for j in range(len(lst_sqr[i])):
            print(lst_sqr[i][j], end=' ')
        print()
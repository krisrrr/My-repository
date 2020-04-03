def main():
    print('Это программа получающая на вход число n и')
    print('выводящая таблицу размером n x n, заполненную')
    print('числами от 1 до n^2 по спирали, выходящей из левого')
    print('верхнего угла и закрученной по часовой стрелке')
    print('Введите любое целое число, большее нуля...')
    n, x = int(input()), 1
    count_of_nums = n ** 2                                     # инициализация переменных
    table = [[0 for i in range(n)] for i in range(n)]
    for l in range(n):                                  # первая сторона (строка 1)
        table[0][l] = x
        x += 1
        if x > count_of_nums: break
    for k in range(round((2 * n - 1) / 4)):
        for i in range(1 + k, n - k):                          # 2, 6, 10, ... стороны
            table[i][n - 1 - k] = x
            x += 1
        if x > count_of_nums: break
        for j in range(-2 - k, -n - 1 + k, -1):                # 3, 7, 11, ... стороны
            table[n - 1 - k][j] = x
            x += 1
        if x > count_of_nums: break
        for i in range(-2 - k, -n + k, -1):                # 4, 8, 12, ... стороны
            table[i][k] = x
            x += 1
        if x > count_of_nums: break                        # 5, 9, 13, ... стороны
        for j in range(1 + k, n - 1 - k):
            table[1 + k][j] = x
            x += 1
    for item in table:
        print(*item)
if __name__ == '__main__':
    main()
def fibonacci_with_list(n: int) -> int:
    '''Функция нахождения числа Фибоначчи
    c сохранением всех значеий до n в массив'''
    f = [0, 1]
    for i in range(2, n + 1):
        f.append(f[i-1] + f[i-2])
    return f[n]

def fibonacci_recursion(n: int) -> int:
    '''Функция нахождения числа Фибоначчи
    c помощью рекурсии'''
    if n <= 1:
        return n
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

def fibonacci_while(n: int) -> int:
    '''Функция нахождения числа Фибоначчи
    без сохранения в массив и с циклом while'''
    f1, f2, i = 0, 1, 0
    if n == 0: return f1
    if n == 1: return f2
    while i <= n-2:
        f1, f2 = f2, f2 + f1
        i += 1
    return f2

def fibonacci_last_digit(n):
    '''Функция нахождения последней цифры числа Фибоначчи'''
    f1, f2, i = 0, 1, 0
    if n == 0: return f1
    if n == 1: return f2
    while i <= n-2:
        f1, f2 = f2 % 10, (f2 + f1) % 10
        i += 1
    return f2

def fibonacci_n_mod_m(n, m):
    '''
    Функция находит остаток от деления
    n-го числа Фибоначчи на m.
    Фишка в том, что мы находим период Пизано для m и
    находит остаток по модулю.
    Например:
    для числа m=4 период Пизано равен 6
    i:         0    1   2   3   4   5|   6   7   8   9   10  11|  12  13  14  15  16      17  |    18
    F_i:       0    1   1   2   3   5|   8   13  21  34  55  89|  144 233 377 610 687     1597|    2584
    F_i mod m: 0    1   1   2   3   1|   0   1   1   2   3   1 |  0   1   1   2   3       1   |    0
                                                         ^
    Таким образом, при n=10 ответ=3, без высчитывания самогочисла Фибоначчи
    '''
    f1, f2, i = 0, 1, 2
    period_list = [0, 1]
    if n == 0: return 0
    if n == 1: return 1
    while i <= n:
        f1, f2 = f2, f2 + f1
        period_list.append(f2 % m)
        if period_list[i - 1] == period_list[0] and period_list[i] == period_list[1]:
            break
        i += 1
    else: return f2 % m
    period = len(period_list) - 2
    mod = period_list[n % period]
    return mod

def GCD_Euclid(n, m):
    '''Функция находит НОД двух чисел
    с помощью алгоритма Евклида'''

    while n != 0 and m != 0:
        if n >= m:
            n = n % m
        else:
            m = m % n
    return n if m == 0 else m
def test():
    #Контейнеры с тестовыми данными
    test_list_0_10 = list(range(11))
    print('Числа Фибоначчи для чисел от 0 до 10 (для каждого числа считается отдельно):')

    print('Число Фибоначчи с сохранением промежуточных значений в массив:')
    print(*[f'F{x} : {fibonacci_with_list(x)}' for x in test_list_0_10], sep='\n')
    print('\n')

    print('Число Фибоначчи с циклом while и без сохранения промежуточных значений:')
    print(*[f'F{x} : {fibonacci_while(x)}' for x in test_list_0_10], sep='\n')
    print('\n')

    print('Число Фибоначчи с помощью рекурсии:')
    print(*[f'F{x} : {fibonacci_recursion(x)}' for x in test_list_0_10], sep='\n')
    print('\n')

    print('Последняя цифра n-го числа Фибоначчи:')
    print(*[f'F{x} : {fibonacci_last_digit(x)}' for x in test_list_0_10], sep='\n')
    print('\n')

    print('Остаток от деления n-го числа на m=4:')
    print(*[f'F{x} : {fibonacci_n_mod_m(x, 4)}' for x in test_list_0_10], sep='\n')
    print('\n')

    print('Наибольший общий делитель двух чисел:')
    print('НОД двух чисел:')
    print(f'НОД 14159572 и 63967072 равен {GCD_Euclid(14159572, 63967072)}')
    print(f'НОД 18 и 35 равен {GCD_Euclid(18, 35)}')
    print(f'НОД 1465432155 и 5689846525 равен {GCD_Euclid(1465432155, 5689846525)}')

if __name__ == "__main__":
    test()

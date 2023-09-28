from typing import List, Tuple
from collections import Counter
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

def fibonacci_last_digit(n: int) -> int:
    '''Функция нахождения последней цифры числа Фибоначчи'''
    f1, f2, i = 0, 1, 0
    if n == 0: return f1
    if n == 1: return f2
    while i <= n-2:
        f1, f2 = f2 % 10, (f2 + f1) % 10
        i += 1
    return f2

def fibonacci_n_mod_m(n: int, m: int) -> int:
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

def GCD_Euclid(n: int, m: int) -> int:
    '''Функция находит НОД двух чисел
    с помощью алгоритма Евклида'''

    while n != 0 and m != 0:
        if n >= m:
            n = n % m
        else:
            m = m % n
    return n if m == 0 else m

def point_cover(m: List[Tuple[int, int]]) -> Tuple[int, list[int]]:
    '''Функция находит минимальное множество точек, которые
    есть во всех отрезках (в каждом отрезке должна быть минимум одна точка)
    Пример:
    Входные данные:
    На вход даются отрезки:
    4 7
    1 3
    2 5
    5 6
    Выходные данные:
    На выход дается минимальное количество точек, которые
    есть во всех отрезках
    (2, [3, 6])
    '''
    sorted_m = sorted(m, key=lambda x: x[1])
    res = [sorted_m[0][1]]
    for i in sorted_m:
        if i[0] <= res[-1] <= i[1]:
            pass
        else:
            res.append(i[1])
    return len(res), res

def continuous_knapsack_problem(v: int, m: List[Tuple[int, int]]) -> float:
    '''Задача на непрерывный рюкзак
    (от каждого предмета можно отделить любую часть, стоимость и объём при этом пропорционально уменьшатся)
    Пример:
    Входные данные:
    На вход даются объем рюкзака и список кортежей цена/объем предмета:
    50
    60 20
    100 50
    120 30
    Выходные данные:
    На выход дается максимальная сумма цен предметов, которые поместятся в рюкзак
    180.0
    '''
    sorted_m = sorted(m, key=lambda x: x[0]/x[1], reverse=True)
    res = 0
    for i in sorted_m:
        if v - i[1] < 0:
            res += i[0] / i[1] * v
            return res
        res += i[0]
        v -= i[1]
    return res

def number_of_different_syllables(k: int) -> Tuple[int, List[int]]:
    '''По данному числу найдите максимальное число k, для которого
    n можно представить как сумму k различных натуральных слагаемых.
    Пример:
    Входные данные:
    6
    Выходные данные:
    Число слагаемых и сами слагаемые
    6
    1 2 3
    '''
    res = []
    for i in range(1, k+1):
        if k - i < i + 1:
            if k - i == 0:
                res.append(i)
                break
            continue
        k -= i
        res.append(i)
    return len(res), res
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
    print('\n')

    print('Задача: покрыть отрезки точками')
    print(f'При входных данных [(4,7), (1,3), (2,5), (5,6)] ответ: {point_cover([(4,7), (1,3), (2,5), (5,6)])}, \n'
          f'тоесть минимум две точки, точка 3 и точка 6 (не единственно верный набор точек)')
    print('\n')

    print('Задача на непрерывный рюкзак')
    print(f'При входных данных объем рюкзака = 50, предметы = [(60, 20), (100, 50), (120, 30)] ответ: '
          f'{continuous_knapsack_problem(50, [(60, 20), (100, 50), (120, 30)])}')
    print('\n')

    print('Задача на подсчет максимального количества различных слагаемых числа k')
    print(f'При входных данных k=6 ответ: {number_of_different_syllables(6)}')
    print('\n')

if __name__ == "__main__":
    test()

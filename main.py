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

def test():
    #Контейнеры с тестовыми данными
    test_list_0_10 = list(range(11))
    print('Числа Фибоначчи для чисел от 0 до 10 (для каждого числа считается отдельно):')
    print('Числа Фибоначчи с сохранением промежуточных значений в массив:')
    print(*[f'F{x} : {fibonacci_with_list(x)}' for x in test_list_0_10], sep='\n')
    print('\n')
    print('Числа Фибоначчи с циклом while и без сохранения промежуточных значений:')
    print(*[f'F{x} : {fibonacci_while(x)}' for x in test_list_0_10], sep='\n')
    print('\n')
    print('Числа Фибоначчи с помощью рекурсии:')
    print(*[f'F{x} : {fibonacci_recursion(x)}' for x in test_list_0_10], sep='\n')
    print('\n')








if __name__ == "__main__":
    test()

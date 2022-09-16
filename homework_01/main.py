"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*n):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [i**2 for i in n] 

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(a):
    if a < 2:
        return False
    f = True
    for i in range(2,a//2+1):
        if a%i == 0:
            f = False
            break        
    return f


def filter_numbers(n,mode):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if mode == 'odd':
        return list(filter(lambda i: i % 2 == 1,n))
    elif mode == 'even':
        return list(filter(lambda i: i % 2 == 0,n))        
    else:
        return list(filter(is_prime,n))

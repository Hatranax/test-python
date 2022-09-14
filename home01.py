#отредактируйте объявленные функции, чтобы они выполняли требуемые действия:
#функция, которая принимает N целых чисел и возвращает список квадратов этих чисел
#Например: power_numbers(1, 2, 5, 7) вернёт [1, 4, 25, 49]
#функция, которая на вход принимает список из целых чисел, и возвращает только чётные/нечётные/простые числа (выбор производится передачей дополнительного аргумента).
#Например: filter_numbers([1, 2, 3], ODD) вернёт [1, 3], а filter_numbers([2, 1, 3, 5, 4], EVEN) вернёт [2, 4]
#необходимо использовать созданные константы ODD/EVEN/PRIME для проверок на тип фильтра (то есть делать не if filter_type == 'odd', а if filter_type == ODD и т.д.)
#рекомендуется использовать встроенную функцию filter
#рекомендуется создать отдельную функцию is_prime в общей области видимости (над функцией filter_numbers) для проверки одного числа, простое ли это число, и использовать её внутри filter_numbers
#не создавайте функцию is_prime (или подобную), которая принимает список из чисел и возвращает список из чисел. Лучше создать функцию is_prime, которая принимает одно число и возвращает True / False

def power_numbers(*n):
    return [i**2 for i in n] 

print(power_numbers(1,2,5,7))

ODD = 1
EVEN = 2
PRIME = 3

def is_prime(a):
    f = True
    for i in range(2,a//2+1):
        if a%i == 0:
            f = False
            break        
    return f

def filter_numbers(*n):
    if n[-1] == 1:
        return list(filter(lambda i: i % 2 == 1,n[0]))
    elif n[-1] == 2:
        return list(filter(lambda i: i % 2 == 0,n[0]))        
    else:
        return list(filter(is_prime,n[0]))

print(filter_numbers([1, 2, 3,4,5,6,7,8,9,10],PRIME))

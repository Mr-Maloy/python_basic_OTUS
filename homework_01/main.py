"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num**2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(num):
    k = 0
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            k += 1
    if k == 0:
        return num


def filter_numbers(nums_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if filter_type == ODD:
        return [num for num in nums_list if num % 2 != 0]
    elif filter_type == PRIME:
        return [num for num in nums_list if is_prime(num)]
    elif filter_type == EVEN:
        return [num for num in nums_list if num % 2 == 0]

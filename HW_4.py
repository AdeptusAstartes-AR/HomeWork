# Задача 1
"""

from sys import argv

scrypt_name, name, time, salary, bonus = argv
try:
    time = int(time)
    salary = int(salary)
    bonus = int(bonus)
    res = time * salary + bonus
    print(f'заработная плата сотрудника  {res}')
except ValueError:
    print('Not a number')
"""
# Способ 2
"""
def sal():
    try:
        time = float(input('Выработка в часах '))
        salary = int(input('Ставка'))
        bonus = int(input('Премия'))
        res = time * salary + bonus
        print(f'Заработная плата сотрудника составляет  {res}')
    except ValueError:
        return print('Not a number')
print(sal())
"""
# Способ 3
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--time', type = float )
parser.add_argument('--salary', type = int )
parser.add_argument('--bonus', type = int )

args = parser.parse_args()

res = (args.time)*(args.salary) + (args.bonus)

print(f' Заработная плата сотрудника составляет {res}')


# Задача 2
"""
my_list = [15, 2, 3, 1, 7, 5, 4, 10]
my_new_list = [el for num, el in enumerate(my_list) if my_list[num - 1] < my_list[num]]
print(f'Исходный список {my_list}')
print(f'Новый список {my_new_list}')
"""
# Задача 3
"""
print(f'Числа от 20 до 240 кратные 20 или 21 - {[el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]}')
"""
# Задача 4
"""
my_list = [1, 4, 4, 2, 3, 2, 8, 10, 8, 5]
my_new_list = [el for el in my_list if my_list.count(el) < 2]
print(my_new_list)
"""
# Задача 5
"""
from functools import reduce


def my_func(el_p, el):
    return el_p * el

print(f'Список четных значений {[el for el in range(99, 1001) if el % 2 == 0]}')
print(f'Результат перемножения всех элементов списка {reduce(my_func, [el for el in range(99, 1001) if el % 2 == 0])}')
"""
# Задача 6
"""
from itertools import count

for el in count(int(input('Введите стартовое число '))):
    print(el) # внимание - беконечный цикл!

from itertools import cycle

my_list = [True, 'ABC', 123, None]
for el in cycle(my_list):
    print(el) # внимание - беконечный цикл!
"""
# Задача 7
"""
rom itertools import count
from math import factorial

def fibo_gen():
    for el in count(1):
        yield factorial(el)

gen = fibo_gen()
x = 0
for i in gen:
    if x < 15:
        print(i)
        x += 1
    else:
        break
"""
# задача 1
"""
arg1 = int(input('Введите первый аргумент'))
arg2 = int(input('Введите второй аргумент'))
def my_func(arg1, arg2):
    try:
        result = arg1 / arg2

    except ZeroDivisionError:
        print('Что-то идет не так')
        result = 0
    else:
        return arg1 / arg2

print(my_func(arg1, arg2))
"""

# задача 2
"""
name = input('Введите имя')
surname = input('Введите фамилию')
date_of_birth = input('Введите год рождения')
town = input('Введите город проживания')
email = input('Введите электронную почту')
phone = input('Введите номер телефона')

def my_task (name, surname, date_of_birth, town, email, phone):
   return ' '.join([name, surname, date_of_birth, town, email, phone])
print(my_task(name, surname, date_of_birth, town, email, phone))
"""
# Задача 3
"""
arg_1 = int(input('Введите первый аргумент'))
arg_2 = int(input('Введите второй аргумент'))
arg_3 = int(input('Введите третий аргумент'))
def my_func(arg1 , arg2, arg3):
    if arg1 >= arg3 and arg2 >= arg3:
        return arg1 + arg2
    elif arg1 > arg2 and arg1 < arg3:
        return arg1 + arg3
    else:
        return arg2 + arg3

print(my_func(arg_1,arg_2, arg_3))
"""
# Задача 4
"""первый способ
x = int(input("Ввведите возводимое число"))
y = int(input("Введите степень"))
def my_func(x, y):
    return x**y
print(my_func(x,y))
"""
# второй способ
"""
x = int(input("Ввведите возводимое число"))
y = int(input("Введите значение степени(отрицательное)"))
def my_func(x, y):
    res = 1
    while y > 0:
        res = 1 / res * x
        y = y - 1
    return res = 1/ res * x
print(my_func(x,y))

#Пример из интернета
def power(x, y):
    res = 1
    for i in range(abs(y)):
        res = res* x
    if y >= 0:
        return res
    else:
        return 1 / res
 
 
print(power(float(input("Первое значение - ")), int(input("Второе значение - "))))
"""
#Задача  6

def int_func (*args):
    word = input("Input words ")
    print(word.title())
    return
int_func()

# Задача 6






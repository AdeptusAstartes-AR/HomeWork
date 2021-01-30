"""
def square(x): # квадрат числа
    print('Квадрат числа', x, '=', x**2)

for i in range(1,11):
    square(i)

def multiply(a,b): # умножение чисел
    print(a*b)

multiply(3,4)

def even(c): # четность чисел
    if c % 2 == 0:
        print(c, "Четное")
    else:
        print(c, "Нечетное")

for k in range(20,31):
    even(k)


def factorial(n):
    pr = 1
    for l in range(2, n+1):
        pr = pr*l
    print(pr)

factorial(4)

if 5 > 1:
    def primer():
        print('hello')
else:
    def primer():
        print('Hello')

primer()


def s_calc():
    r_val = float(input("Укажите радиус: "))
    h_val = float(input("Укажите высоту: "))
    # площадь боковой поверхности цилиндра:
    s_side = 2 * 3.14 * r_val * h_val
    # площадь одного основания цилиндра:
    s_circle = 3.14 * r_val ** 2
    # полная площадь цилиндра:
    s_full = s_side + 2 * s_circle
    return s_full

s_val = s_calc()
print(s_val)

"""
"""
x = int(input("Ввведите возводимое число"))
def square(x):
    return x**2

a = square(x)
print(a)
"""


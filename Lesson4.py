"""
try:
    print('Try to open')
    f = open('lesson_5.txt', 'b')
except ZeroDivisionError:
    print('No!')
finally:
    f.close()
    print('Closed')
"""
"""
with open ('lesson_5.txt') as f:
    data = f.writelines(['potato\n', 'egg'])

with open('lesson_5.txt') as f:
    data = f.readlines()

print(data[o])
"""
"""
import os
import numpy
print(numpy.array([1,2,3])) # простой список приводим к списку данных numpy
print(type(numpy.array([1,2,3]))) # определяем тип списка
"""
# arg parser
"""
from  sys import argv
script_name, name, surname = argv # присваиваем переменной argv переменные
print(f'Our args are {argv}. It is type {type(argv)}, {type(argv[1])}') #  печатеам argv переменную  печатает все аргументы,  тип , тип одного из аргументов
print(f'Hello worker,{name} {surname}')
"""
"""
from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type = str )
parser.add_argument('--age', type = int )
parser.add_argument('--data_path', type = str )
parser.add_argument('--place', type = str, default='shop' )

args = parser.parse_args()
print(f'In our args{args}. Type {type(args.age)}')
print(f'Hello,{args.name}. Your age {args.age}. Ypu work in {args.place}')
"""
#import os
import os
files = os.listdir('/home/sedochka/2 класс')
#print(files)
#path = os.getcwd()
#print(path)
#os.mkdir('test_folder')
os.rmdir('test_folder')

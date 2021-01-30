"""
from sys import argv

from argparse import ArgumentParser

parser = ArgumentParser()

parser.add_argument('--name', type = str)
parser.add_argument('--age', type = int)
parser.add_argument('--data_path', type = int, default= None)
parser.add_argument('--place', type = str, default = 'shop')

args = parser.parse_args()

print(f'Hello, {args.name}! You are {args.age}. You work in {args.place}')
"""
import random
import time
import ast
import os
#for i in range(5):
 #   print(f'hello. It is {i}')
  #  time.sleep(10)


#files = os.listdir()
#path = os.getcwd()
#os.mkdir('test_folder')
#print(path)
#print(files)

#ids= [12, 17, 16, 90, 25, 86]

#print(random.sample(ids,2))
#random.shuffle(ids)
#print(ids)
"""
random_str = ['cat', 'dog', 'mouse']
new_random_list = []
for el in random_str:
    new_random_list.append(el.title())
print(new_random_list)

better_new_random_str = [el.title() if el.isdigit() == False else el for el in random_str]
print(better_new_random_str)
"""
def my_gen(num):
    for el in range(num):
        yield el
x= my_gen(6)
y= my_gen(6)
print([el for el in x])
print([el for el in y])


from functools import reduce
def my_f(symbol_1, symbol_2):
    return symbol_1 + symbol_2
random_str = ['a', 'b', 'c', 'd']
print(reduce(my_f, random_str))

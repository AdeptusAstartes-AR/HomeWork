#print('hello world')
#print('hello me')
#print('enough')


my_list1 = [5, 'text', True, None, 136.3]
for i in my_list1:
    print(f'{i} is {type(i)}')

numb = int(input('Введите число элементов'))
my_list2 = []
i = 0
el = 0
while i < numb:
    my_list2.append(input("Введите следующий элемент"))
    i += 1

for el in range(int(len(my_list2)/2)):
    my_list2[el], my_list2[el+1] = my_list2[el+1], my_list2[el]
    el = el + 2
print(my_list2)

my_str = input("введите строку ")
my_word = []
num = 1
for el in range(my_str.count(' ') + 1):
    my_word = my_str.split()
    if len(str(my_word)) <= 10:
        print(f" {num} {my_word [el]}")
        num += 1
    else:
        print(f" {num} {my_word [el] [0:10]}")
        num += 1


seasons_list = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1: 'winter', 2: 'spring', 3: 'summer', 4: 'autumn'}
month = int(input("Введите месяц по номеру "))
if month == 1 or month == 12 or month == 2:
        print(seasons_dict.get(1))
        print(seasons_list[0])
elif month == 3 or month == 4 or month == 5:
    print(seasons_dict.get(2))
    print(seasons_list[1])
elif month == 6 or month == 7 or month == 8:
    print(seasons_dict.get(3))
    print(seasons_list[2])

elif month == 9 or month == 10 or month == 11:
    print(seasons_dict.get(4))
    print(seasons_list[3])
else:
        print("Такого месяца не существует")

number = int(input("Enter number: "))
my_list3 = [7, 4, 3, 2]
c = my_list3.count(number)
for element in my_list3:
    if c > 0:
        i = my_list3.index(number)
        my_list3.insert(i+c, number)
        break
    else:
        if number > element:
            j = my_list3.index(element)
            my_list3.insert(j, number)
            break
        elif number < my_list3[len(my_list3) - 1]:
            my_list3.append(number)
print(my_list3)

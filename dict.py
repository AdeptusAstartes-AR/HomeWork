"""
d = { #словарь
    'Moskva': 495,
    'Piter': 812,
    'Penza':8412
}
a = [['Moskva', 495], ['Piter', 812], ['Penza', 8412]] # создание словаря способ
r = dict(Moskva = 495, Piter = 812, Penza = 8412) # создание словаря, только если ключ строковый
t = dict(a)
q = dict.fromkeys(['a', 'b', 'c'], 100) #способ создания словаря если нужно всем ключам дать одинаковые данные
print(f' Первый способ:{r}, \n Второй способ: {q}, \nТретий способ: {t}')
"""
"""
d ={
    1 : "one",
    2: "two",
    3: "three"
}

#d[4] = 'four' #добавление ключа и значения, несуществуюему ключу присваиваем значение
print(d[3]) #обращение к значению по ключу
"""
"""
 заполнение словаря
person = {} # пустой словарь
s = 'Ivanov Ivan Samara  SGU 5 4 4 5 5 3 4 5'
s = s.split() # разбивка по пробелам и создание списка
person['last name'] = s[0]
person['First name'] = s[1]
person['Town'] = s[2]
person['University'] = s[3]
person['marks'] = []
for i in s[4:]:
    person['marks'].append(int(i))
print(person)
"""
d ={
    1 : "one",
    2: "two",
    3: "three"
}
print(d)
# del d[1]  #удаление по ключу
print(d.get(4, 'No such el')) # обращение к ключу и в случае отсутствия присваивает новое указанное
d.setdefault(7, 'seven') #передача нового ключа и значения или новое значение сущ ключу
print(d)
print(len(d)) # длина словаря
print (1 in d) #проверка наличия ключа в словаре
#for key in d:
#    print(key, d[key])

# try\except
def calc(m):
    # 1000:10 = m:x
    try:   #задаем программе проверить на интовое значение
        m = int(m)
    except Exception:
        print('Something wrong')
    return 10*m/1000
print(calc('6000'))
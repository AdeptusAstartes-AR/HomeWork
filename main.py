"""
name = 'Семен'
midname = "Семенович"
balance = 36.82
def f(x):
    return  x**2
text = f" Дорогой {name.lower()}  {midname.upper()}, баланс вашего лицевого счета составлет {f(5)} руб."
print(text)
"""
"""
d = {
"name" : 'Семен',
"midname" : "Семенович",
"balance" : 36.82
}
text = f" Дорогой {d['name']}  {d['midname']}, баланс вашего лицевого счета составлет {d.get('balance')} руб."
print(text)
"""
gender = {
    'm': 'Дорогой',
    'f': 'Дорогая'
}
a = (
    ['Седа', 'Ашотовна', 32.56,'f'],
    ['Евгений', 'Леонидович', 25.78, 'm'],
    ['Александр', 'Константинович', 128.93, 'm']
)
for name, midname, balance, gen in a:
    text = f" {gender[gen]} {name}  {midname}, баланс вашего лицевого счета составлет {balance} руб."
    print(text)

"""
name = 'Семен'
midname = "Семенович"
balance = 36.82
def f(x):
    return  x**2
text = f" Дорогой {name.lower()}  {midname.upper()}, баланс вашего лицевого счета составлет {f(5)} руб."
print(text)
"""

d = {
"name" : 'Семен',
"midname" : "Семенович",
"balance" : 36.82
}
text = f" Дорогой {d['name']}  {d['midname']}, баланс вашего лицевого счета составлет {d['balance']} руб."
print(text)
print(text)
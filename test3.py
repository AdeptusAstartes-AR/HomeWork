price_rub = 1500
#eur_cost = float(input('Введите курс евро'))
eur_cost = 88
price_euro = price_rub / eur_cost
greetings = f"I am the first programm"
type_of_variable = type(greetings)
print(f'This is price in rub: {price_rub}')
print(f'this is price in euro: {price_rub // eur_cost} and cents {round(price_rub % eur_cost)}')
# определение типа аргумента  print(type_of_variable)
#test_v = 10
# преобразование во флоат
# print(float(test_v))
# булевая переменная
# test_bool = True
# печать булевого значения и преобразование в целочисленное(True=1 False=0)
# print(f'{test_bool}, {int(test_bool)}')
'''
первый способ проверки цены с двойным if
if  price_euro < 15:
    if price_euro > 10:
        print('in next month')
    else:
        print('buy')
else:
    print('Price too high')
'''
# второй способ с пом elif движемся от выше 15 до 0
if price_euro > 15:
    print('Price is too high')
elif price_euro <= 10 and price_euro >=0:
    print('buy it')
else:
    print('next month')

# циклы
while price_euro > 10:
      price_euro -= 0.5 # price_euro = price_euro - 0.5
      print(f'we update cost {price_euro}')
      break #останавливаем после первого цикла

# flag_x = True
item = None
while item != 'freedom':
   item = input("What do you want")
  # if item == "freedom":
   #    print('You are free')
    #   flag_x = False
      # или  break  если условие выполнилось - останавливаем цикл

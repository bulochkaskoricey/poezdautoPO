import main



if main.city_one+ main.city_two == 'МоскваСочи':
    print = ("Стоимость билета: 2000 рублей")
    pay = input("Оплатить ?")
    
elif main.city_one+ main.city_two == 'МоскваАдлер':
    stoim = ('Стоимость билета: 3000 рублей')
    pay = input("Оплатить ?")
    
elif main.city_one+ main.city_two == 'МоскваАнапа':
    stoim = ('Стоимость билета: 3000 рублей')
    pay = input("Оплатить ?")
    
else:
    print("Такого маршрута нету !")
    exit = input ("Вернуться назад ?")


if pay == 'Да':
    import SimpleQIWI
    print(SimpleQIWI)

elif pay == 'Нет':
    print("Хорошо не в этот раз !")
    exit = input ("Вернуться к главному меню ?")
    
else:
    print("Такого ответа нет !")
    exit = input ("Вернуться назад ?")
    
    
if exit == 'Да':
    print("Хорошо")
    print(main.osnov)
    
elif exit == 'Нет':
    print("Окей")
    print(main.osnov)
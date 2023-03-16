from pyowm import OWM
import main



owm = OWM('825cef665073edbb21d9f7d82d226b4d')


mgr = owm.weather_manager()
observation = mgr.weather_at_place(main.OWM_Mark)
w = observation.weather


#температура
t = w.temperature("celsius")
t1 = t['temp']
t2 = t['feels_like']
t3 = t['temp_max']
t4 = t['temp_min']
#скорость ветра
wi = w.wind()['speed']
#Влажность
humi = w.humidity
#облачность
cl = w.clouds
#время
ti = w.reference_time('iso')

watter = (f"В городе {main.OWM_Mark} температура {t1}, ощущается как {t2}, максимальная темпа {t3}, минимальная темпа {t4}")


print(watter)


if t1 < 5:
    print("На улице достаточно холодно, лучше одеться теплее.")
elif t1 > 15:
    print("На улице тепло.")
elif t1 < 1:
    print("На улице очень холодно, стоит одеться тепло.")
else:
    print("На улице очень тепло.")


exit = input("Вернуться назад ?")




if exit == 'да':
    import main
    print("Хорошо")
    print(main)


elif exit == 'нет':
    import main
    print("Хорошо")
    print(main)


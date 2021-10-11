def Calc(a):
    s = 0
    b = 0
    c = a
    while a > 0:
        b = int(a % 10)
        if(b % 2 == 0):
            s = s + b
        a = int(a / 10)
    print ("Сумма четных цифр в числе",c, "равна", s )


try:
    a = int(input("Введите десятизначное число: "))
except ValueError:
    print('ошибка')
if len(str(a)) == 10:
    Calc(a)
else:
    print("Так нельзя")
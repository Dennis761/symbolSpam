n = input("Введіть своє число: ")
for number in n:
    i = 0
    x = ''
    while i < int(number):
        i += 1
        x += '#'
    print(x)
#1. Спочатку створюємо змінну n, яка буде приймати
# аргументом стрічку введену користувачем
#2.1 Потім ітеруємо кожен член цієї стрічки за
# допомогою цикла for/in 
#2.2 Всередині цього циклу ми вводимо змінні i, х
# та ще один новий цикл while
#3.1 За допомогою цього нового цикла ми можемо додавати
# змінну х саму до себе числу, рівному змінній number. 
#3.2 Змінна number була перетворена в число за допомогою
# функції int()
#4. І в самому кінці ми зможемо вивести результат 
# кількості символів '#' у кожну стрічку консолі
# Висновок: на цій лабораторній роботі я засвоїв використання 
# основних циклів for/in, while та їхню взаємодію у мові програмування
# python, я точно знаю, що ці знання знадобляться мені у майбутньому
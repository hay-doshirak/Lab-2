import random
print("Математика для детей")
counter = 0
mistakes = 0
while mistakes<3:
    num1 = random.randrange(11)
    num2 = random.randrange(11)
    rez = num1+num2
    x = "Реши пример: " + str(num1) + "+" + str(num2) + "="
    otvet=int(input(x))
    if otvet==rez:
        counter+=1
        print("Правильно!")
    else:
        mistakes+=1
        print("Ответ неверный.")
print("Игра окончена. Правильных ответов: ", counter)
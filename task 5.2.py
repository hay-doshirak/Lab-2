print("Водите слова для записи в строку. Чтобы прервать введите: стоп или stop.")
s = ""
while True:
    w = str(input("Введите слово: "))
    if w.lower() == "stop" or w.lower() == "стоп":
        break
    else: s = s + w + " "
print(s)


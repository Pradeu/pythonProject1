try:
    a = input('Введите имя файла:')
    text = open(f"{a}", mode="r")
    s = list()
    for i in range(int(text.readline())):
        c = text.readline().rstrip('\n')
        if c == '':
            continue
        else:
            s.append(int(c))
    print(s)
except FileNotFoundError:
    print("Такого файла нет!")
except ValueError:
    print("Ошибка в значении параметра файла!")
else:
    text.close()

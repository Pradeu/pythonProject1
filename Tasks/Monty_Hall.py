import random
a = [0, 1, 0]
summa = 0
total = 1000000
#random(a)
for i in range(total):
    d = a.copy()
    b = random.randint(0, 2)
    if b == 0:
        d.pop(2)
    else:
        d.pop(0)
    if d[0] == 1:
        summa = summa + 1
percent = summa/total * 100
print(f"Процент выигрыша равен {percent}")


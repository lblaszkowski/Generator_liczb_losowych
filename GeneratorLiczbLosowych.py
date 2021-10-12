import random

lotto = []
od_liczby = 1
do_liczby = 5
ilosc_liczb_do_wylosowania = 5
i = 0

while i < ilosc_liczb_do_wylosowania:
    r = random.randint(od_liczby, do_liczby)
    if lotto.count(r) == 0:
        lotto.append(r)
        i+=1
print(lotto)
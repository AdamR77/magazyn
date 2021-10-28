
from typing import NamedTuple
from decimal import Decimal

class MyTuple(NamedTuple):
    count: int
    name: str
    unit: str
    price: Decimal
    amount: int



items_list = []
#amount = []

#pobieranie danych: name, unit, price, amount
count = 1
while True:
    print("")
    print(f'Nazwa towaru [{count}]:', end =" ")
    name = input()
    if name == 'end':
        print('pobieranie danych zakończone')
        break
    print("")
    print(f'jednostka ceny towaru [{name}]: 1.[pln/kg] czy 2.[pln/szt.]: ')
    while True:
        try:
            unit_choice = int(input('twój wybór: '))    
        except:
            print('wybór poza kryterium ')
        else:
            if unit_choice == 1:
                unit = '[pln/kg]'
                break
            if unit_choice == 2:
                unit = '[pln/szt.]'
                break
            print('proszę podać liczbe 1 lub 2 odpowiadające jednostce ceny ')
               

    while True:
        print("")
        print(f'podaj cenę towaru [{name}]:', end = " ")
        price = input()
        try:
            round(float(price),2)
        except:
            print('cena musi być liczbą >= 0')    
        else:    
            if float(price) < 0:
                print('cena nie może być ujemna')
            if float(price) >= 0:    
                break         
        #print('cena musi być liczbą >= 0')

    while True:
        print("")
        print(f'podaj ilość towaru [{name}]: ', end = " ")
        amount = input()
        try:
            int(amount)
        except:
            print('ilośc musi być liczbą całkowitą >= 0')
        else:
            if int(amount) < 0:
                print('podaj ilość >= 0')
            break
    price = float(price)
    amount = int(amount)
    parameters = MyTuple(count, name, unit, price, amount) 
    items_list.append(parameters)   
    count += 1
print(items_list)
print('Lp.\tTowar\tjednostka\tcena\tilość ')
print('---\t-----\t---------\t----\t----- ')
for t in items_list:
    print(f' {t.count}\t{t.name}\t{t.unit}\t{t.price}\t{t.amount}')


#    for parameter in item:
#        print(f'{parameter}\t', end="")
#    print("")




    
    






    
        



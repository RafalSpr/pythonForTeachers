'''
Porównanie działania dwóch funkcji sprawdzających,
czy dana liczba jest pierwsza, dla liczby 
n = 179424691
'''
from datetime import *

def pierwszaSzybciej(a):
    '''
    Funkcja sprawdza, czy liczba jest pierwsza przeglądając liczby od 2 do pierwiastka z a
    '''
    if a <=1: #oczywiście 1 nie jest pierwsza ;-)
        return False
    i=2
    while (i*i<=a): # lub alternatywnie i<=sqrt(a)
        if (a % i==0): #znalazłem dzielnik, liczba nie jest pierwsza
            return False
        i = i + 1
    return True #skoro liczba nie ma dzielników właściwych, więc musi być pierwsza

def pierwszaWolniej(a):
    '''
    Metoda brute force, czyli przeglądam wszystkie liczby od 2 do a-1
    '''
    if a <=1: #oczywiście 1 nie jest pierwsza ;-)
        return False
    for i in range(2,n):
        if n % i ==0: #znalazłem dzielnik, liczba nie jest pierwsza
            return False
    return True #skoro liczba nie ma dzielników właściwych, więc musi być pierwsza
    
n = 179424691

start = datetime.now()
print(pierwszaSzybciej(n))
end = datetime.now()
czas= end-start
#czas działania pierwszej funkcji
print("Czas działania pierwszej funkcji w sek. ",czas.seconds)


start = datetime.now()
print(pierwszaWolniej(n))
end = datetime.now()
czas= end-start
#czas działania drugiej funkcji
print("Czas działania drugiej funkcji w sek. ",czas.seconds)


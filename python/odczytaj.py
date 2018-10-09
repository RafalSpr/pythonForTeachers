plik=open("dane.txt","r")
lista=[]
for i in plik:
    lista.append((i))
wynik=open("wynik.txt","w")
lista.sort()
zbior=set()
zbior=set(lista)
wynik.writelines(lista)
plik.close()
wynik.close()

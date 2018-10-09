import random
plik=open("dane.txt","w")
for i in range(1000):
    plik.write(str(random.randint(1,500)))
    plik.write("\n")
plik.close()

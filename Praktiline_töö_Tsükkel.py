from math import *
from random import *
#0
p=0
while True:
    number = int(input("Sisestage number suurem kui: "))
    p+=1
    if number >= 10:
        print("Õigesti")
        break
    else:
        print("Arv on liiga väike")
print("katsed",p)




#22 (1)
print("Ma tahan kommi")
katsed=0
while True:
    answer=input("Ma tahan kommi!")
    katsed +=1
    if answer.lower() == "komm":
        print(f"Teil kommid kirutatakse kulus {katsed} katse.")
        break

#22 (2)
katsed=0
answer=""
while answer!="komm":
    answer=input("Ma tahan kommi!")
    katsed +=1
print(f"Katsed: {katsed}")
print()
  



#11 ülisane 
print("Arvuti mõistatab numbrit 1-10 ja sina üritad seda ära arvata.")
a=randint (1,10)
vastus=int(input("mis arv on mõistatanud arvutit?: "))
k=p=1
while vastus!=a:
    print("Ära sa ei arvanud ära , proovi uueati!:")
    vastus=int(input("Sisesta vastus: "))
    k+=1
    p+=1
    if k>2:
        print("Püüdlused on lõppenud")
        b=input("Proovi veel kord")
        if b.upper()=="JAH":
            k=1
            continue
        else:
            break
if vastus==a:
    print("Palju õnne, sa arvasid ära!",p )

print()



from math import *
from random import *
for i in range (1,5):
    x=str("*"*i).center (18, " ")
    print(x, end="")
    print()
for i in range (1,7):
    x=str("*"*(i+2)).center (18, " ")
    print(x, end="")
    print()
for i in range (1,10):
    x=str("*"*(i+4)).center (14, " ")
    print(x, end="")
    print()


#harjutus 6
#1
n=0
print ("kolmnurga")
for e in range (11,0,-1):
    n= n + 1
    for f in range (1, n+1):
        print("*", end = "")
        print()
    print ("")
    #2
    for x in range (5):
        print("******")
    #3
    print ("kolmnurga")
for e in range (11,0,-1):
    n= n - 1
    for h in range (0, n-1):
        print("*", end = "")
        print()
    print ("")


#(3)
from math import * 
from random import *
print ("Sisestage number")
x=float(input())
while 10:
  print (x)
x += 1
while type(n) != int:
 
        n = int(n)


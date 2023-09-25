# pentru a crea o lista in python, ii dam denumirea listei apoi semnul = [iar aici scrim elementele listei]
"""
A = [1,2,3,4,5,6,7,8,9]
for x in A:
    print(x)

# Pentru a putea trece prin elementele liste, anume dupa indexul lor putem folosi urmatorul algoritm

for i in range(len(A)):
    A[i] = A[i] * A[i]
print(A) # output [1, 4, 9, 16, 25, 36, 49, 64, 81]
# aici am trecut prin indexul fiecarui element din lista si l-am ridicat pa patrat apoi l-am afisat la ecran

# pentru a crea o lista cu un numar anumit de elemente putem folosi urmatorul algoritm

B = [0] * 100
# am creat o lista B cu o 100 de elemente maxime
# mai jos vom crea un algoritm de adaugare a elementelor in lista B
top = 0
x = int(input("Introdu un numar: "))
# atita timp cit x este diferit de 0 sa se intimple urmatoarele
while x != 0:
    B[top] = x
    top += 1
    x = int(input("Introdu din nou un numar: "))
print("Numarul de elemente in lista este: ", top)
# afisam toate numelere introduse la ecran
for i in range(top):
    print(B[i])
"""
# pentru a copia 2 liste putem folosi urmatorul algoritm

N = int(input("Introdu numarul de elemente care va contine lista: "))
Lista_1 = [0] * N
Lista_2 = [0] * N
for k in range(N):
    Lista_1[k] = int(input("Introdu un numar in lista: "))

# mai departe copiem toate elementele din Lista_1 in Lista_2

for i in range(N):
    Lista_2[i] = Lista_1[i]


print("Lista nr 1 este: ",Lista_1) # output Lista nr 1 este:  [5, 6, 9, 1, 2, 352, 15, 15, 7, 9]
print("Lista nr 2 este: ", Lista_2)# output Lista nr 2 este:  [5, 6, 9, 1, 2, 352, 15, 15, 7, 9]

# sau putem sa copiem listele prin urmatorul mod
Lista_3 = list(Lista_1)
print("Lista nr 3 este: ",Lista_3) # output Lista nr 3 este:  [12, 45, 78, 96, 32]
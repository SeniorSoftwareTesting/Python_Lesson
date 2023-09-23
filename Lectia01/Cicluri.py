# ciclul while
# while conditie:
#   operator1
#   operator2
#   operatorN

# in python se foloseste identarea pentru a putea vedea un bloc de cod, identarea are 4 spatii sau un tab
x = 10
while x > 2:
    print(x)
    x -= 1

# acum vom vorbi despre conditia if elif si else
y = 6
if y < 10:
    print("y este mai mic ca 10")
elif y == 10:
    print("y este egal cu 10")
else:
    print(" y este mai mare ca 10")

# ciclul for se foloseste pentru a itera un bloc de cod de un anumit numar de ori 
for _ in range(5):
    print("Acest text se printeaza de 5 ori")
# operatii in python
#1 adunare scadere , inmultire, impartire
nr1 = 2
nr2 = 4
nr3 = 5
adunare = nr1 + nr2  #6
scadere = nr2 - nr1  #2
inmultire = nr1 * nr2 * nr3  # 40
impartire = nr3 / nr1  # 2.5
# ridicarea la putere
exponent = nr3**nr2

# calcularea radicalului
radical = nr2**0.5

print(adunare)
print(scadere)
print(inmultire)
print(impartire)

# impartire fara rest sau x div y
div = nr3 // nr2
print(div)  # 1  5/4 = 1

# pentru a vedea restul impartirii folosim operatia %
restul_impartirii = nr3 % nr2
print(restul_impartirii)  #1 5/2 rest 1


# mai exista si scurtaturi la adunare, inmultire etc
# putem folosi o prescurtare x+=1 echivalent ca x = x + 1, la fel se procedeaza pentru toate operatiile

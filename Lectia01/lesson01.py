# acesta este un comentariu
# pentru a printa ceva la ecran folosim comanda print("aici scrim tot ce vrem sa afiseze la ecran sau consola")
print("Primul program pe python")
# variabile in python sunt de mai multe tipuri
# crearea variabilelor are loc in urmatoarea forma: nume variabila = valoare
# variabila de tip int
numar = 1
# variabila de tip float 
numar1 = 2.34
# variabila de tip str
nume = " Ion "
# pentru a vedea tipul variabilei introducem comanda print(type(denumirea variabilei))
print("Variabila numar este de tip:")
print(type(numar)) # output <class 'int'>




# schimbarea variabilei prin a 3-a variabila
a = 2
b = 3
temp1 = a
print("a este: ",a,", b este: ",b,", temp1 este: ",temp1)
a = b
b = temp1
print("a este: ",a,", b este : ",b)



# mai putem crea mai multe variabile intr-o singura linie
x,y,z=4,5,6
# aici x=4, y=5, z=6

#putem sa schimbam valoarea a 2-a variabile fara a 3-a variabila
nr = 3
nr1 = 45
nr,nr1 = nr1,nr
print("nr este: ",nr,", nr1 este: ",nr1)
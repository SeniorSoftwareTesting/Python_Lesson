def cautare_numar(A:list,N:int,x:int):
    """Cauta numarul x in lista A de la 0 
        la N-1 inclusiv. Returneaza indexul numarului x
        in lista A 
    """
    for k in range(N):
        if A[k] == x:
            return k
    return -1
# aici A este lista, N reprezinta numarul de elemente in lista
# iar x reprezinta numarul care trebuie de cautat in lista

def test_cautare_numar():
    A1= [1,2,3,4,5]
    m = cautare_numar(A1,5,9)
    if m ==-1:
        print("Test 1 - OK")
    else:
        print("Test 2 - Fail")

    A2= [-1,-2,-3,-4,-5]
    m = cautare_numar(A2,5,-3)
    if m ==2:
        print("Test 2 - OK")
    else:
        print("Test 2 - Fail")

    A3= [10,20,30,10,25]
    m = cautare_numar(A3,5,10)
    if m ==0:
        print("Test 3 - OK")
    else:
        print("Test 3 - Fail")

test_cautare_numar()
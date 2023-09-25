def invers_list(A:list, N:int):
    """Inverseaza lista de la ultimul element
        pana la primul
    """
    for i in range(N//2):
        A[i],A[N-1-i] = A[N-1-i],A[i]


def test_invers_list():
    B1 = [1,2,3,4,5,6,7,8,9,10]
    print("Lista pana la inversare: ",B1)
    invers_list(B1,len(B1))
    print("Lista dupa inversare:    ",B1)
    if B1 == [10,9,8,7,6,5,4,3,2,1]:
        print(" Test 1 - Ok")
    else:
        print("Test 1 - Fail")
    
    B2 = [0,0,0,0,0,5]
    print("Lista pana la inversare: ",B2)
    invers_list(B2, len(B2))
    print("Lista dupa inversare:    ",B2)
    if B2 == [5,0,0,0,0,0]:
        print(" Test 2 - Ok")
    else:
        print("Test 2 - Fail")
test_invers_list()

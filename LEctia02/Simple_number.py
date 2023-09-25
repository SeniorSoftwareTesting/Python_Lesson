def simple_number(x):
    """Verifica daca un numar este prim sau nu """
    divizor = 2
    while divizor < x:
        if x % divizor == 0:
            return False
        divizor += 1
    return True

print(simple_number(19))
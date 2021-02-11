def seqsum():
    n = int(input())
    nr = 0
    if n != 0:
        nr = nr + n
        seqsum()
    return print(nr)


seqsum()

def seqsum():
    global nr
    n = int(input())
    if n != 0:
        nr = nr + n
        seqsum()
    elif n == 0:
        print(nr)


nr = 0
seqsum()

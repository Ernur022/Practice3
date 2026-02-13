def muf(n):
    return lambda a : a * n
mud = muf(2)
print(mud(11))
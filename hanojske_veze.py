def Vez(n,z, do, s):
    if n >= 1:
        Vez(n-1,z,s,do)
        Disk(z,do)
        Vez(n-1,s,do,z)

def Disk(z,d):
    print("Přesuň disk",z,"do",d)

Vez(3,"A","B","C")
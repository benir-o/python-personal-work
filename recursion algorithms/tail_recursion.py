def tailsum(n,acc=0):
    if n==0:
        return acc
    else:
        return tailsum(n-1,acc+n)
print(tailsum(3))
'''
For tail recursion, the recursive call is the last thing that happens
during our return statement.
'''


def tailsum(n,acc=0):
    if n==0:
        return acc
    else:
        return tailsum(n-1,acc+n)
print(tailsum(3))
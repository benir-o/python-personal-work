'''
For indirect recursion, two functions call each other until the base case is
hit
'''


def function1(n):
    if n>=0:
        print('A: ',n)
        function2(n-1)
    else:
        print("done")

def function2(n):
    if n>0:
        print('B: ',n)
        function1(n-1)
    else:
        print("done")

function1(3)
'''
For head recursion, the recursive call happens first before any
other thing in the function
'''

def head_recursion(n):
    if n==0:
        return
    head_recursion(n-1)
    print(n)
head_recursion(3)
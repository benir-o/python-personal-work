'''
For head recursion, the recursive call happens first before any
other thing in the function
'''

def head_recursion(n):
    if n==0:
        return "done"
    else:
        print(n)
        return head_recursion(n-1)

print(head_recursion(3))
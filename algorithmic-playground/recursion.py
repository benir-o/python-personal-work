print("Hello World")
'''
In direct recursion, a function
calls itself directly.

For indirect recursion,a function calls another function
which eventually calls the original function back.
'''

def countdown(n):
    if n<=0:
        print("Done!")
    else:
        print(n)
        countdown(n-1) # direct call to itself

countdown(3)

def funcA(n):
    if n>0:
        print('A: ',n)
        funcB(n-1)# Function calling another function

def funcB(n):
    if n>0:
        print('B: ',n)
        funcA(n-1) #Function calling another function

funcA(3)

'''
Tail recursion-> A recursion where the recursive call is
the last thing that happens in the function
This means that there's nothing left to do after the call returns

Head recursion-> The recursive call happens first, before any other
operations in the function
This means that the function waits for the recursive call to finish before
doing anything else

'''

def tail_sum(a, acc=0):
    if a==0:
        return acc
    else:
        return tail_sum(a-1,acc+a)
    # Here the last operation is the tailsum(a-1,acc+a)
    #Hence it is a tail recursion
print("Tail recursion\n----------")
print(tail_sum(3))

def head_recursion(k):
    if k==0:
        return
    head_recursion(k-1)# recursive call happens first
    print(k) # action done after the recursive call

print("Head recursion\n-----------")
head_recursion(3)


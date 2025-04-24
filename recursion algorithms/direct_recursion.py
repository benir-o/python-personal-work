'''
For direct recursion, a function calls itself directly.
'''
def countdown(n):
    if n<=0:
        print("Done")
        return #ensures the function terminates once the base case is hit
    else:
        print(n)
        countdown(n-1)
countdown(3)

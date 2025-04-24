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
        # we print then call, the stack prints as it gets full?
countdown(3)


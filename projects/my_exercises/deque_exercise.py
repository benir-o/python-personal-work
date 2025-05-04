from collections import deque



my_stack= deque([10,15,20,25])

my_stack.rotate(4)
print(my_stack)
print(my_stack.rotate(4)==my_stack.rotate(-4))
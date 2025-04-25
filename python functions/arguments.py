'''
Keyword arguments vs non-keyword arguments
'''
def mydictionary(**kwargs):
     return kwargs

def mysum(*args):
    return sum(args)
print(mysum(1,2,4,5))
print(mydictionary(name='Juliani', age=21, school='Strathmore'))
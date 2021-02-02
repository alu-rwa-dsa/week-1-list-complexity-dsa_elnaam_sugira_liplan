#second question
from memory_profiler import profile

@profile(precision=4)

def add2(a,b):
    result = a+b
    return result

print(add2(2,3))

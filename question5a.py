import timeit  


mysetup = "from math import sqrt"

mycode = '''  
ls = [1,3,44,5,2]
maxVal = ls[0]

for i in range (0, len(ls)):
    if maxVal < ls[i] :
        maxVal = ls[i]
    
print(maxVal)
'''

print(timeit.timeit(setup=mysetup, stmt=mycode, number=1000))
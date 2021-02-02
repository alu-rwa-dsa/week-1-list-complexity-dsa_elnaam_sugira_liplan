import timeit  
  
mysetup = "from math import sqrt"

mycode = '''  

word = 'Three'

print(word.lower())
'''

print(timeit.timeit(setup=mysetup, stmt=mycode, number=1000)) 
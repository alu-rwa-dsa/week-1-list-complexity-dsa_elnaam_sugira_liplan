import timeit  
  

mysetup = "from math import sqrt"
  

mycode = '''  

ls = [1,3,4,3,5,6,7,66,43,23]
ls.sort()
print(ls)

'''
  
print(timeit.timeit(setup=mysetup, stmt=mycode, number=1000)) 
#first question
import time

start = time.time()
n = 0
while True:
    print("Hello")
    n = n + 1
    if n == 10000:
        break

end = time.time()
time_n = end - start
print("Time taken is: ")
print(time_n)

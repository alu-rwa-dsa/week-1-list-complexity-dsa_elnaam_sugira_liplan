from time import time
from matplotlib import pyplot as plt
from guppy import hpy
import string
import random
from question3a import FindMax
from question3b import ToLower
from question3c import SortLs


# Plot a graph showing how the time and space taken as the input size changes from length 1 to length 100.

# Algorithm 1
# Time Graph
# create list of length 100
created_list = [i for i in range(1, 101)]


# create function that records time taken for each input size
def take_time(array):
    time_taken = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        FindMax(sub_list)
        end_time = time()
        time_diff = end_time - start_time
        time_taken.append(time_diff)
    return time_taken


times_taken = take_time(created_list)

# plot graph
plt.title("Input Size vs Time taken")
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.plot(created_list, times_taken)
plt.show()

# ii.Space graph

# creating session context
h = hpy()


# create function that records space used for each input size
def take_space(array):
    space_taken = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        h.setrelheap()
        FindMax(sub_list)
        raw_string = repr(h)
        raw_string = raw_string.split()
        space = raw_string[10]
        space_taken.append(space)
    return space_taken


spaces_taken = take_space(created_list)

# plot graph
plt.title("Input Size vs Space taken")
plt.xlabel("Input size")
plt.ylabel("Space taken")
plt.plot(created_list, spaces_taken)
plt.show()

# Algorithm 2
# Time Graph
# create random string of uppercase letters of length 100
created_word = string.ascii_uppercase
created_long_word = (''.join(random.choice(created_word) for i in range(100)))


# create function that records time taken for each input size
def take_time(array):
    time_taken = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        ToLower(sub_list)
        end_time = time()
        time_diff = end_time - start_time
        time_taken.append(time_diff)
        
    return time_taken


times_taken = take_time(created_long_word)

# plot graph
plt.title("Input Size vs Time taken")
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.plot(created_long_word, times_taken)
plt.show()

# Space Graph


# creating session context
h = hpy()


# create function that records space used for each input size
def take_space(array):
    space_taken = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        h.setrelheap()
        ToLower(sub_list)
        raw_string = repr(h)
        raw_string = raw_string.split()
        space = int(raw_string[10])
        space_taken.append(space)
    return space_taken


spaces_taken = take_space(created_word)

# plot graph
plt.title("Input Size vs Space taken")
plt.xlabel("Input size")
plt.ylabel("Space taken")
plt.plot(created_word, spaces_taken)
plt.show()

# Algorithm 3
# Time Graph
# create list of length 100
created_int_list = random.sample(range(1, 100), 100)


# create function that records time taken for each input size
def take_time(array):
    time_taken = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        SortLs(sub_list)
        end_time = time()
        time_diff = end_time - start_time
        time_taken.append(time_diff)
    return time_taken


times_taken = take_time(created_int_list)

# plot graph
plt.title("Input Size vs Time taken")
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.plot(created_int_list, times_taken)
plt.show()

# Space Graph
# creating session context
h = hpy()


# create function that records space used for each input size
def take_space(array):
    space_taken = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        h.setrelheap()
        SortLs(sub_list)
        raw_string = repr(h)
        raw_string = raw_string.split()
        space = int(raw_string[10])
        space_taken.append(space)
    return space_taken


spaces_taken = take_space(created_word)

# plot graph
plt.title("Input Size vs Space taken")
plt.xlabel("Input size")
plt.ylabel("Space taken")
plt.plot(created_int_list, spaces_taken)
plt.show()

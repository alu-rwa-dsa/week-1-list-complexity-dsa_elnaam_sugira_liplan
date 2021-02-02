from time import time
from matplotlib import pyplot as plt
from guppy import hpy
import random
from question3a import FindMax
from question3b import ToLower
from question3c import SortLs

# Question 1
# Time Graph
# create list of length 100
cr_ls = [i for i in range(1, 101)]


# create function
def tk_tm(array):
    tk_tmn = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        FindMax(sub_list)
        end_time = time()
        tm_df = end_time - start_time
        tk_tmn.append(tm_df)
    return tk_tmn


tms_tkn = tk_tm(cr_ls)

# plot graph
plt.title("Input Size vs Time taken for FindMax")
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.plot(cr_ls, tms_tkn)
plt.show()

#Space graph

# creating session context
h = hpy()


# create function
def tk_sp(array):
    sp_tkn = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        h.setrelheap()
        FindMax(sub_list)
        raw_string = repr(h)
        raw_string = raw_string.split()
        space = raw_string[10]
        sp_tkn.append(space)
    return sp_tkn


sps_tkn = tk_sp(cr_ls)

# plot graph
plt.title("Input Size vs Space taken Find Max")
plt.xlabel("Input size")
plt.ylabel("Space taken")
plt.plot(cr_ls, sps_tkn)
plt.show()


# Question 3
# Time Graph
# create list of length 100
cr_int_ls = random.sample(range(1, 101), 100)

# create function


def tk_tm(array):
    tk_tmn = []

    for i in range(1, len(array) + 1):
        sub_list = array[0:i]
        start_time = time()
        SortLs(sub_list)
        end_time = time()
        tm_df = end_time - start_time
        tk_tmn.append(tm_df)
    return tk_tmn


tms_tkn = tk_tm(cr_int_ls)

# plot graph
plt.title("Input Size vs Time take Sortls")
plt.xlabel("Input size")
plt.ylabel("Time taken")
plt.plot(cr_int_ls, tms_tkn)
plt.show()

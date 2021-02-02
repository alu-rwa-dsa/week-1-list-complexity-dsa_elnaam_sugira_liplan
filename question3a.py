elnaam_work


def FindMax(l):
    maxVal = l[0]
    for i in range(0, len(l)):
        if maxVal < l[i]:
            maxVal = l[i]
    return maxVal

ls = [1, 3, 44, 5, 2]
FindMax(ls)




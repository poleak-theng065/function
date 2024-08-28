def max(array):
    max = 0
    for i in array:
        if i > max:
            max = i
    return max
print(max([2,3,5,0,11,5,2]))

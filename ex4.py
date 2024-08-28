def min(array):
    min = array[0]
    for i in array:
        if i < min:
            min = i
    return min
print(min([2,3,5,0,11,5,2]))
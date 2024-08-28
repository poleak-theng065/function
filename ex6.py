def count(array):
    count = 0
    for i in array:
        if i >= 0:
            count += 1
    return count
print(count([-1,11,2,0,-1,4]))
def count(array):
    count = 0
    for i in array:
        if i == 5:
            count += 1
    return count
print(count([2,3,5,0,11,5,2]))
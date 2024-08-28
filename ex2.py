def sum(array):
    sum = 0
    for i in array:
        if i % 2 == 1:
            sum += i
    return sum
print(sum([1,2,3,4,5,6]))
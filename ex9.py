def average(array):
    average = 0
    sum = 0
    count = 0
    for i in array:
        if "price" in i:
            sum += i["price"]
            count += 1
    average = sum / count
    return average
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(average(products))
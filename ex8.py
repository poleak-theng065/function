def total(array):
    total = 0
    for i in array:
        if "price" in i:
            total += i["price"]
    return total
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(total(products))
            
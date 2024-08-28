def max(array):
    max = 0
    product = ""
    for i in array:
        if i["price"]>=max:
            product = i["name"]
            max = i["price"]
    return product
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(max(products))
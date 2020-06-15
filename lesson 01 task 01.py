list_of_numbers = [1, 3, 5, 7, 9]

r = list_of_numbers[3]
print(r)

products = {
    'cherry': 110,
    'strawberry': 100,
    'cucumber': 40
}

cherry_price = products['cherry']
strawberry_price = products['strawberry']
tomato_price = products.get('cucumber', 0)
print(tomato_price)


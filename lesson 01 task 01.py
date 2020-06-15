from random import randint

i = 0
list_of_even = []
size = 30

while i < size:
    temp_int = randint(1, 300)
    # print(temp_int)
    if not (temp_int % 2):
        list_of_even.append(temp_int)
        i += 1
    else:
        continue

print(list_of_even)



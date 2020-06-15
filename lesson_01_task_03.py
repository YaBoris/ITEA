limit = 100
i = 1

while i <= limit:
    if not i % 3:
        print('Fizz')
    if not i % 5:
        print('Buzz')
    if not i % 15:
        print('FizzBuzz')
    if i % 3 and i % 5 and i % 15:
        print(i)
    i += 1

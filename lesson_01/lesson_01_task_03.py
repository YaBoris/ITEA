limit = 100
i = 1

for i in range(limit+1):
    if not i % 15:
        print('FizzBuzz')
    elif not i % 3:
        print('Fizz')
    elif not i % 5:
        print('Buzz')
    else:
        print(i)

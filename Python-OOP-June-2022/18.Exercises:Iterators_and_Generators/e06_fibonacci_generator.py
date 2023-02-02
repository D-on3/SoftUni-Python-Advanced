def fibonacci():
    first_num = 0
    second_num = 1
    yield first_num
    yield second_num

    while True:
        next_num = first_num + second_num
        first_num, second_num = second_num, next_num
        yield next_num


generator = fibonacci()
for i in range(5):
    print(next(generator))
generator = fibonacci()
for i in range(1):
    print(next(generator))

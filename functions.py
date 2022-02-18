def call_numbers():
    for number in range(0, 10):
        print(number)


def call_numbers_with_limit(limit):
    list = range(0, 10)
    # for number in    list[limit]:
    for number in range(limit):
        print(number)


call_numbers_with_limit(50)

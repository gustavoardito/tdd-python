def fizz_buzz(value):
    return (
        'FizzBuzz' if is_multiple(value, 5) else 'Fizz'
    ) if is_multiple(value, 3) else (
        'Buzz' if is_multiple(value, 5) else str(value)
    )


def is_multiple(value, mod):
    return value % mod == 0


def fizz_buzz(value):
    return str(value) if value % 5 != 0 and value % 3 != 0 else (
        '{}{}'.format(
            'Fizz' if value % 3 == 0 else '',
            'Buzz' if value % 5 == 0 else '',
        )
    )


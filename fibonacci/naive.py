def fibonacci_naive(number) -> int:
    if number == 0 or number == 1:
        return number
    else:
        return fibonacci_naive(number - 2) + fibonacci_naive(number - 1)

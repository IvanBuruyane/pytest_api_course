def fibonacci_dynamic(n: int) -> int:
    fib_list = [0, 1]
    for i in range(1, n + 1):
        fib_list[0], fib_list[1] = fib_list[1], fib_list[0] + fib_list[1]
    return fib_list[0]

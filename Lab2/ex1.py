def fibonacci(n):
    fibonacci_sequence = [1, 1]

    while len(fibonacci_sequence) < n:
        next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_number)

    return fibonacci_sequence[:n]


n = int(input("n = "))
result = fibonacci(n)
print(result)

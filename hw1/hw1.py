import ast

import networkx


def fibonacci(n):
    numbers = [0, *range(1, n)]
    for i in range(2, n):
        numbers[i] = numbers[i - 1] + numbers[i - 2]

    return numbers


if __name__ == '__main__':
    print(fibonacci(10))

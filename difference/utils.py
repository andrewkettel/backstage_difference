def sum_of_squares(n: int) -> int:
    sum_of_squares: int = 0
    for i in range(1, n + 1):
        sum_of_squares += i * i

    return sum_of_squares


def square_of_sums(n: int) -> int:
    sum_of_number = sum(range(1, n + 1))
    return sum_of_number * sum_of_number


def calculate_difference(n: int) -> int:
    return abs(sum_of_squares(n) - square_of_sums(n))

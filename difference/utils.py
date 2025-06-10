def sum_of_squares(n: int) -> int:
    # efficient O(1) instead of O(n) loop
    # https://www.cuemath.com/algebra/sum-of-squares/
    return (n * (n + 1) * (2 * n + 1)) // 6


def square_of_sums(n: int) -> int:
    # efficient O(1) instead of O(n) loop
    # https://www.cuemath.com/sum-of-natural-numbers-formula/
    sum_of_numbers = n * (n + 1) // 2
    return sum_of_numbers * sum_of_numbers


def calculate_difference(n: int) -> int:
    return abs(sum_of_squares(n) - square_of_sums(n))

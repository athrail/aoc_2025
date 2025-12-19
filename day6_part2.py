import re
from typing import Tuple
from itertools import pairwise


def parse_table_from_input(input: str) -> Tuple[list[list[str]], list[int]]:
    lines = input.strip("\n").split("\n")
    table = []

    # To get column widths you can count amount of spaces between operators from the last line
    operators = lines[-1]
    indexes = [i for i, c in enumerate(operators) if c == "*" or c == "+"]
    widths = [b - a - 1 for a, b in pairwise(indexes)]
    widths.append(len(operators) - indexes[-1])

    # based on the widths parse columns into a table
    for line in lines[:-1]:
        for i, w in enumerate(widths):
            start = sum(widths[:i], 0) + i
            number = line[start : start + w]
            if len(table) > i:
                table[i].append(number)
            else:
                table.append([number])

    operators = re.sub(r"\s+", " ", operators.strip()).split(" ")
    for i, col in enumerate(table):
        col.append(operators[i])

    return table, widths


def solve_table(table: list[list[str]], widths: list[int]) -> int:
    total = 0

    for i, col in enumerate(table):
        op = col[-1]
        col_total = 0 if op == "+" else 1

        for j in range(widths[i]):
            number = ""
            for row in col[:-1]:
                number += row[j]

            if op == "*":
                col_total *= int(number)
            elif op == "+":
                col_total += int(number)

        total += col_total

    return total


def solution() -> int:
    with open("./input_day6.txt", "r") as f:
        table, widths = parse_table_from_input(f.read())
        return solve_table(table, widths)


print(solution())


def test_day6_part2():
    input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

    table, widths = parse_table_from_input(input)
    result = solve_table(table, widths)

    assert 3263827 == result

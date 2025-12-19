import re


def parse_table_from_input(input: str) -> list[list[str]]:
    lines = input.splitlines()
    line = lines[0]
    line = re.sub(r"\s+", " ", line.strip())
    numbers: list[list[str]] = [[number] for number in line.split(" ")]

    for line in lines[1:]:
        cleared = re.sub(r"\s+", " ", line.strip())
        line_numbers = cleared.split(" ")
        for i, n in enumerate(line_numbers):
            numbers[i].append(n)

    return numbers


def solve_table(table: list[list[str]]) -> int:
    total = 0

    for col in table:
        op = col[-1]
        col_total = 0 if op == "+" else 1
        for n in col[:-1]:
            if op == "*":
                col_total *= int(n)
            elif op == "+":
                col_total += int(n)
        total += col_total

    return total


def solution() -> int:
    with open("./input_day6.txt", "r") as f:
        table = parse_table_from_input(f.read())
        return solve_table(table)


print(solution())


def test_day6_part1():
    input = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

    table = parse_table_from_input(input)
    result = solve_table(table)

    assert 4277556 == result

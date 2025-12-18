#! /usr/bin/env python
from typing import Tuple


def move_rolls(table: list[list[str]]) -> list[Tuple[int, int]]:
    """
    Counts how many rolls can be moved and removes them from the table
    """

    def get_adjacent_rolls(
        x: int, y: int, table: list[list[str]], max_x: int, max_y: int
    ) -> int:
        found_rolls = 0

        for y_check in range(y - 1, y + 2):
            if y_check < 0 or y_check >= max_y:
                continue

            for x_check in range(x - 1, x + 2):
                if x_check >= 0 and x_check < max_x:
                    if x_check == x and y_check == y:
                        continue

                    if table[y_check][x_check] == "@":
                        found_rolls += 1

        # print(f"Found rolls for ({x},{y}) = {found_rolls}")
        return found_rolls

    max_x = 0
    max_y = len(table)
    coords = []

    for y, row in enumerate(table):
        max_x = len(row)
        for x, c in enumerate(row):
            if c == "@" and get_adjacent_rolls(x, y, table, max_x, max_y) < 4:
                # print(f"Movable roll @ ({x},{y})")
                coords.append((x, y))

    return coords


def solution() -> int:
    with open("./input_day4.txt", "r") as f:
        input = f.read()

        table = [[c for c in line] for line in input.strip().splitlines()]
        coords = move_rolls(table)
        movable = len(coords)

        while len(coords) > 0:
            for coord in coords:
                table[coord[1]][coord[0]] = "."
            coords = move_rolls(table)
            movable += len(coords)

        return movable


def test_day4():
    input = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""
    table = [[c for c in line] for line in input.strip().splitlines()]
    coords = move_rolls(table)
    movable = len(coords)

    while len(coords) > 0:
        for coord in coords:
            table[coord[1]][coord[0]] = "."
        coords = move_rolls(table)
        movable += len(coords)

    assert movable == 43


solution()

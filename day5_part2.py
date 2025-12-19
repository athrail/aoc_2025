# hangs and runs out of RAM :o
from dataclasses import dataclass
from functools import reduce


def count_ingredient_ids(lines: list[str]) -> int:
    ranges = []

    @dataclass
    class Range:
        start: int
        end: int

        def __str__(self):
            return f"Range({self.start}, {self.end})"

        def __repr__(self):
            return f"Range({self.start}, {self.end})"

    # Remove duplicates before parsing (but only from range definitions)
    lines = list(set(lines[: lines.index("\n")]))

    # Gather ranges
    for line in lines:
        line = line.strip()
        if "-" in line:
            [start, end] = line.split("-")
            ranges.append(Range(int(start), int(end)))
        elif line == "":
            break

    # Check for overlaps
    ranges = sorted(ranges, key=lambda r: r.start)
    print(ranges[:10])
    to_delete = []
    last = None

    for r in ranges:
        if last is None:
            last = r
            continue

        if r.start <= last.end:
            if last.end < r.end:
                last.end = r.end
            to_delete.append(r)
        else:
            last = r

    # Delete subranges
    for r in to_delete:
        ranges.remove(r)

    print(ranges)

    # Count ids through substraction
    return sum(r.end - r.start + 1 for r in ranges)


def solution() -> int:
    with open("./input_day5.txt", "r") as f:
        return count_ingredient_ids(f.readlines())


def test_day5_part2():
    input = """3-5
10-14
16-20
12-18
9-21

1
3
"""

    assert 16 == count_ingredient_ids(input.splitlines(True))  # ty:ignore[invalid-argument-type]


def test_day5_part2_test2():
    input = """10-20
5-10
11-15

1
3
"""

    assert 16 == count_ingredient_ids(input.splitlines(True))  # ty:ignore[invalid-argument-type]

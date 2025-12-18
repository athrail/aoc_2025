def count_fresh(lines: list[str]) -> str:
    ranges = []
    fresh = 0

    for line in lines:
        line = line.strip()
        if "-" in line:
            [start, end] = line.split("-")
            ranges.append((int(start), int(end)))
        elif line == "":
            continue
        else:
            ingredient = int(line)
            for check_range in ranges:
                if ingredient >= check_range[0] and ingredient <= check_range[1]:
                    fresh += 1
                    break
    return fresh


def solution() -> int:
    with open("./input_day5.txt", "r") as f:
        return count_fresh(f.readlines())


def test_day5_part1():
    """
    For input
    3-5
    10-14
    16-20
    12-18

    1
    5
    8
    11
    17
    32

    Result should be 3
    """
    input = "3-5\n10-14\n16-20\n12-18\n\n1\n5\n8\n11\n17\n32"

    assert 3 == count_fresh(input.splitlines())

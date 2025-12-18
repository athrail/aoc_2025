#! /usr/bin/env python


def get_bank_max_joltage(bank: str) -> int:
    digits = [int(c) for c in bank.rstrip()]
    count = len(digits)
    print(digits)
    indexes = []
    print(indexes)

    indexes.append(0)

    value = "".join([str(digits[i]) for i in indexes])
    print(f"{value}")
    return int(value)


def sum_joltage(banks: list[str]) -> int:
    total = 0

    for bank in banks:
        total += get_bank_max_joltage(bank)

    return total


def test_day3():
    banks = """
987654321111111
811111111111119
234234234234278
818181911112111
"""
    banks = banks.strip()
    split_banks = banks.splitlines()

    assert 3121910778619 == sum_joltage(split_banks)


def solution() -> int:
    with open("./input_day3.txt", "r") as f:
        banks = f.readlines()

    return sum_joltage(banks)


solution()

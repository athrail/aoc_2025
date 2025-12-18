#! /usr/bin/env python


from functools import reduce


def get_bank_max_joltage(bank: str) -> int:
    max = -1

    for i in range(len(bank)):
        for j in range(len(bank) - 1, i, -1):
            value = int(bank[i] + bank[j])
            max = value if value > max else max

    return max


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

    assert 357 == sum_joltage(split_banks)


def solution() -> int:
    with open("./input_day3.txt", "r") as f:
        banks = f.readlines()

    return sum_joltage(banks)


solution()

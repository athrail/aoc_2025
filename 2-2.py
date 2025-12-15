#! /usr/bin/env python


from functools import reduce


def check_id_range(range_descriptor: str) -> list[str]:
    [start, end] = range_descriptor.split("-")
    invalid_ids: list[str] = []

    for id in range(int(start), int(end) + 1):
        stringified_id = str(id)
        half_of_length = len(stringified_id) // 2

        for i in range(1, half_of_length + 1):
            check = stringified_id[:i]
            times = len(stringified_id) // i
            if check * times == stringified_id:
                invalid_ids.append(stringified_id)
                print(f"Found invalid ID: {stringified_id}")
                break

    return invalid_ids


def test_day2():
    input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"
    expects = {
        "11-22": ["11", "22"],
        "95-115": ["99", "111"],
        "998-1012": ["999", "1010"],
        "1188511880-1188511890": ["1188511885"],
        "222220-222224": ["222222"],
        "446443-446449": ["446446"],
        "38593856-38593862": ["38593859"],
        "565653-565659": ["565656"],
        "824824821-824824827": ["824824824"],
        "2121212118-2121212124": ["2121212121"],
    }

    # input = "565653-565659"
    # expects = {"565653-565659": ["565656"]}
    #
    for range_descriptor in input.split(","):
        invalid_ids = check_id_range(range_descriptor)
        assert invalid_ids == expects.get(range_descriptor, [])


def main():
    invalid_ids = []

    with open("./input_day2.txt", "r") as f:
        input = f.readline()
        for range_descriptor in input.split(","):
            invalid_ids.extend(check_id_range(range_descriptor))

    result = reduce(lambda sum, id: sum + id, [int(id) for id in invalid_ids], 0)
    print(f"Sum of invalid IDs: {result}")


main()

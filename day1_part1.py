#! /usr/bin/env python

# Safe password
# We're getting dial instructions from input file and need to count how many times we hit 0 after any rotation


class Dial:
    def __init__(self) -> None:
        self.position = 50
        self.password = 0

    def rotate(self, instruction: str):
        direction = instruction[0]
        amount = int(instruction[1:])

        print(f"Rotating {direction} by {amount}")
        print(f"Position before {self.position}")
        self.position += (amount % 100) * (-1 if direction == "L" else 1)
        print(f"Position after {self.position}")
        self.position = (
            self.position + 100 if self.position < 0 else self.position % 100
        )
        print(f"Position after2 {self.position}")

        if self.position == 0:
            self.password += 1


def solution() -> int:
    dial = Dial()
    with open("./input_1.txt", "r") as f:
        for i, line in enumerate(f.readlines()):
            dial.rotate(line.strip())

    return dial.password


solution()


def test_dial():
    dial = Dial()
    assert dial.position == 50

    dial.rotate("R1")
    assert dial.position == 51

    dial.rotate("L1")
    assert dial.position == 50

    dial.rotate("R50")
    assert dial.position == 0

    dial.rotate("L50")
    assert dial.position == 50

    dial.rotate("L50")
    assert dial.position == 0

    dial.rotate("L1")
    assert dial.position == 99


def test_dial_aoc():
    dial = Dial()

    actions = [
        ("L68", 82),
        ("L30", 52),
        ("R48", 0),
        ("L5", 95),
        ("R60", 55),
        ("L55", 0),
        ("L1", 99),
        ("L99", 0),
        ("R14", 14),
        ("L82", 32),
    ]

    for action in actions:
        dial.rotate(action[0])
        assert dial.position == action[1]

    assert dial.password == 3

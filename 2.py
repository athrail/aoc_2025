#! /usr/bin/env python

# Safe password
# We're getting dial instructions from input file and need to count how many times we hit 0 after any rotation
# Additionally need to count every click that happens on 0


class Dial:
    def __init__(self) -> None:
        self.position = 50
        self.password = 0

    def rotate(self, instruction: str):
        direction = instruction[0]
        amount = int(instruction[1:])

        self.password += amount // 100
        amount = amount % 100

        old_position = self.position
        self.position += amount * (-1 if direction == "L" else 1)

        if old_position != 0 and (self.position < 0 or self.position > 100):
            self.password += 1

        self.position = (
            self.position + 100 if self.position < 0 else self.position % 100
        )

        if self.position == 0:
            self.password += 1


def main():
    dial = Dial()
    with open("./input_1.txt", "r") as f:
        for line in f.readlines():
            dial.rotate(line.strip())

    print(f"Safe password is {dial.password}")


main()


def test_dial():
    dial = Dial()
    assert dial.position == 50
    assert dial.password == 0

    dial.rotate("R1")
    assert dial.position == 51

    dial.rotate("L1")
    assert dial.position == 50

    dial.rotate("R50")
    assert dial.position == 0
    assert dial.password == 1

    dial.rotate("L50")
    assert dial.position == 50
    assert dial.password == 1

    dial.rotate("L50")
    assert dial.position == 0
    assert dial.password == 2

    dial.rotate("L1")
    assert dial.position == 99
    assert dial.password == 2


def test_dial_clicks():
    dial = Dial()
    assert dial.position == 50
    dial.rotate("R1000")
    assert dial.position == 50
    assert dial.password == 10

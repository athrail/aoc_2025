from dataclasses import dataclass


def track_and_count_beams(diagram: str) -> int:
    lines = diagram.strip().splitlines()
    start_x = lines[0].index("S")
    live_beams = set()
    finished_beams = 0

    @dataclass
    class Beam:
        x: int
        y: int

        def __hash__(self) -> int:
            return hash(str(self.x) + str(self.y))

    live_beams.add(Beam(start_x, 0))
    print(len(lines))

    while len(live_beams) > 0:
        reached_end = []
        new_beams = []
        for beam in live_beams:
            beam.y += 1

            if beam.y >= len(lines):
                reached_end.append(beam)
                finished_beams += 1
                continue

            print(beam)
            if lines[beam.y][beam.x] == "^":
                new_beams.append(Beam(beam.x + 1, beam.y))
                beam.x -= 1

        (live_beams.remove(b) for b in reached_end)
        live_beams.update(new_beams)

    return finished_beams


def test_day7_part1():
    input = """.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

    assert 21 == track_and_count_beams(input)


test_day7_part1()


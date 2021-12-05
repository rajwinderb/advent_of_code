"""
--- Part Two ---
Unfortunately, considering only horizontal and vertical lines doesn't give you the full picture; you need to also
consider diagonal lines.

Because of the limits of the hydrothermal vent mapping system, the lines in your list will only ever be horizontal,
vertical, or a diagonal line at exactly 45 degrees. In other words:

An entry like 1,1 -> 3,3 covers points 1,1, 2,2, and 3,3.
An entry like 9,7 -> 7,9 covers points 9,7, 8,8, and 7,9.
Considering all lines from the above example would now produce the following diagram:

1.1....11.
.111...2..
..2.1.111.
...1.2.2..
.112313211
...1.2....
..1...1...
.1.....1..
1.......1.
222111....
You still need to determine the number of points where at least two lines overlap. In the above example, this is still
anywhere in the diagram with a 2 or larger - now a total of 12 points.

Consider all of the lines. At how many points do at least two lines overlap?
"""


def get_vents():
    file = open("../inputs/five_puzzle_one_input.txt", "r")
    data_strings = [vent_str.split(' -> ') for vent_str in file.read().split('\n')]
    vents = [[tuple([int(i) for i in vent_end.split(',')]) for vent_end in vent_ends] for vent_ends in
             data_strings[0:-1]]
    return vents


def is_horizontal_or_vertical(vent):
    [(x0, y0), (x1, y1)] = vent
    return (x0 == x1) or (y0 == y1)


def points_in_line_hv(vent):
    [(x0, y0), (x1, y1)] = vent
    if x0 == x1:
        points = [(x0, y) for y in range(min(y0, y1), max(y0, y1) + 1)]
    elif y0 == y1:
        points = [(x, y0) for x in range(min(x0, x1), max(x0, x1) + 1)]
    return points


def points_in_line(vent):
    if is_horizontal_or_vertical(vent):
        return points_in_line_hv(vent)
    # non horizontal or vertical lines
    # diagonally aligned 45 degrees then |x0 - x1| == |y0 -y1|
    [(x0, y0), (x1, y1)] = vent

    if abs(x0 - x1) == abs(y0 - y1):
        xs = range(x0, x1 +
                   1) if x0 < x1 else range(x0, x1 -1, -1)
        ys = range(y0, y1 +
                   1) if y0 < y1 else range(y0, y1 -1, -1)
        points = [(x, ys[i]) for i, x in enumerate(xs)]
        return points


def main():
    vents = get_vents()
    multiple_points = set()
    points = {}
    for vent in vents:
        for point in points_in_line(vent):
            if point in points:
                multiple_points.add(point)
                points[point] += 1
            else:
                points[point] = 1
    print(len(multiple_points))
    return len(multiple_points)


if __name__ == '__main__':
    main()

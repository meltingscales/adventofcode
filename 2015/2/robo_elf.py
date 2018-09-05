def line_to_ints(l='1x1x1'):
    return [int(x) for x in l.split('x')]


def get_sides(ints=[1, 1, 1]):
    all_sides = []

    # Generate all permutations of l,w,h multiplied with eachother.
    for i in range(len(ints)):
        for j in range(len(ints)):
            if (i != j):
                all_sides.append(ints[i] * ints[j])

    return all_sides


def get_face_perimeters(ints=[2, 3, 4]):
    all_fp = []

    for i in range(len(ints)):
        for j in range(len(ints)):

            a = ints[i]
            b = ints[j]

            if (i != j):
                all_fp.append(a + a + b + b)

    return all_fp


def calc_ribbon(ints=[1, 1, 1]):
    l, w, h = ints

    fps = get_face_perimeters(ints)

    lowest = sorted(fps)[0]

    return lowest


def calc_bow(ints=[1 * 1 * 1]):
    x = 1

    for int in ints:
        x *= int

    return x


def calc_needed_area(ints=[1, 1, 1]):
    l, w, h = ints

    all_sides = get_sides(ints)

    smallest_side = sorted(all_sides)[0]

    return ((2 * l * w) + (2 * w * h) + (2 * h * l) + smallest_side)


total_area_no_ribbon = 0
total_area_with_ribbon = 0

with open('input', 'r') as f:
    for line in f.readlines():
        ints = line_to_ints(line)

        area_box = calc_needed_area(ints)
        area_ribbon = calc_ribbon(ints) + calc_bow(ints)

        print(f"{str(ints):15s} = {area_box:10d} box, {area_ribbon:10d} ribb")

        total_area_no_ribbon += area_box
        total_area_with_ribbon += area_ribbon

print(f"Area w/o  ribbon:   {total_area_no_ribbon}")
print(f"Area of ribbons:    {total_area_with_ribbon}")

print(calc_ribbon([2, 3, 4]))
print(calc_ribbon([1, 1, 10]))

assert (total_area_no_ribbon == 1606483)
assert (total_area_with_ribbon == 3842356)

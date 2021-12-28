import os
from functools import reduce
from operator import add
from typing import List


def get_data() -> List[int]:
    lines = []
    with open('../input') as fh:
        lines = fh.readlines()

    # Turn string into integer and remove '\n'
    for i in range(0, len(lines)):
        lines[i] = int(lines[i].strip())

    return lines


def generate_rolling_average(lst: List[int], slice_len: int = 3) -> List[int]:
    averages: List[int] = []

    for i in range(0, len(lst) - (slice_len - 1)):
        slice: List[int] = lst[i:(i + (slice_len - 1)) + 1]

        average = reduce(add, slice)
        averages.append(average)

        print("Average of {} is {}".format(slice, average))

    return averages


if __name__ == '__main__':

    data = get_data()
    averages = generate_rolling_average(data)

    times_increasing = 0
    times_decreasing = 0

    slice_len = 2
    for i in range(0, len(averages) - (slice_len - 1)):

        slice: List[int] = averages[i:(i + (slice_len - 1)) + 1]

        if slice[1] > slice[0]:
            times_increasing += 1
        elif slice[1] < slice[0]:
            times_decreasing += 1

        # print(slice)

    print("times_increasing={}".format(times_increasing))
    print("times_decreasing={}".format(times_decreasing))

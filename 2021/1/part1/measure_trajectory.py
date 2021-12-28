import os
from typing import List


def get_data() -> List[int]:
    lines = []
    with open('../input') as fh:
        lines = fh.readlines()

    # Turn string into integer and remove '\n'
    for i in range(0, len(lines)):
        lines[i] = int(lines[i].strip())

    return lines


lines = get_data()

times_increasing=0
times_decreasing=0

slice_len = 2
for i in range(0, len(lines)-(slice_len-1)):

    slice: List[int] = lines[i:(i+(slice_len-1))+1]
    
    if slice[1] > slice[0]:
        times_increasing+=1
    elif slice[1] < slice[0]:
        times_decreasing+=1

    # print(slice)

print("times_increasing={}".format(times_increasing))
print("times_decreasing={}".format(times_decreasing))
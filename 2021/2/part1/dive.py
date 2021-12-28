from pprint import pprint
from typing import List, Union


def get_data() -> List[str]:
    lines = []
    with open('../input') as fh:
        lines = fh.readlines()

    for i in range(0, len(lines)):
        # remove '\n'
        lines[i] = (lines[i].strip())

        # split into tuple of (op, int)
        tup: List[str, int] = lines[i].split(' ')
        tup[1] = int(tup[1])
        lines[i] = tup

    return lines


def resolve_vector_name(name: str):
    lut = {
        'down': [0, -1],
        'up': [0, 1],
        'forward': [1, 0],
        'backward': [-1, 0]
    }

    return lut[name]


def data_to_vector(datum: List[Union[str, int]]) -> List[Union[int,int]]:
    scalar = datum[1]
    vector = resolve_vector_name(datum[0])

    scaled_vector = []
    for n in vector:
        scaled_vector.append(scalar * n)

    return scaled_vector


def all_data_to_vector(data: List[List[Union[int, str]]]) -> List[List[int]]:

    vectors = []

    for datum in data:
        vectors.append(data_to_vector(datum))

    return vectors

def resolve_vectors_to_position(vecs: List[List[int]])->List[int]:

    pos = [0,0] # x, y

    for vec in vecs:
        pos[0] += vec[0]
        pos[1] += vec[1]

    return pos

data = get_data()
vectors = all_data_to_vector(data)
pos = resolve_vectors_to_position(vectors)

print("Final position: ")
print(pos)

raise Exception("asdf")
from typing import List

# ROCKS=['A','X']
# PAPERS=[]
# SCISSORS=[]

STRATEGY = {
    'A': 'Y',
    'B': 'X',
    'C': 'Z',
}

SHAPE_SCORE = {
    'rock': 1,
    'paper': 2,
    'scissors': 3,
}


def rps_to_points(rps: str) -> int:
    return SHAPE_SCORE[rps]


def beats(shape1, shape2):
    if shape1 == 'rock' and shape2 == 'scissors':
        return True

    if shape1 == 'scissors' and shape2 == 'paper':
        return True

    if shape1 == 'paper' and shape2 == 'rock':
        return True

    return False


def ties(shape1, shape2):
    return shape1 == shape2


def calculate_score(their_move: str, my_move: str) -> int:
    my_move = character_to_rps(my_move)
    their_move = character_to_rps(their_move)

    points = 0

    points += rps_to_points(my_move)

    if ties(my_move, their_move):
        # we tie
        points += 3
    elif beats(my_move, their_move):
        # I win
        points += 6
    elif beats(their_move, my_move):
        # they win
        points += 0

    # print(points)
    return points


def calculate_scores(rps_list: List[List[str]]) -> int:
    score = 0
    for round in rps_list:
        their_move, my_move = round
        score += calculate_score(their_move, my_move)
    return score


def character_to_rps(c: str) -> str:
    if c in ['A', 'X']:
        return 'rock'
    if c in ['B', 'Y']:
        return 'paper'
    if c in ['C', 'Z']:
        return 'scissors'


def read_input() -> List[List[str]]:
    ret = []

    with open('./input', 'r') as f:
        for line in f.readlines():
            line = line.strip()
            ret.append(line.split(' '))

    return ret


assert (calculate_score('A', 'Y') == 8)
assert (calculate_score('B', 'X') == 1)
assert (calculate_score('C', 'Z') == 6)

assert (
        calculate_scores([
            ['A', 'Y'],
            ['B', 'X'],
            ['C', 'Z'],
        ]) == (8 + 1 + 6)
)


input = read_input()

print(input)

print(calculate_scores(input))
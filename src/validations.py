from src.exceptions import *
from typing import List


def validate_start(start_row: List, max_dimens: List) -> None:
    if len(start_row) != 3:
        msg = f'{start_row} not in valid format of X Y C'
        raise BadStartException(msg)
    try:
        x_start = int(start_row[0])
    except ValueError as e:
        msg = f'x coord must be ints: {start_row[0]}'
        raise BadStartException(msg)
    try:
        y_start = int(start_row[1])
    except ValueError as e:
        msg = f'y coord must be ints: {start_row[1]}'
        raise BadStartException(msg)
    cardinal = start_row[2]
    if type(x_start) != int:
        msg = f'x value {x_start} must be int, is {type(x_start)}'
        raise BadStartException(msg)
    if x_start > max_dimens[0]:
        msg = f'Start at x value {x_start} not possible, {max_dimens[0]} max'
        raise OffMapException(msg)
    if type(y_start) != int:
        msg = f'y value {y_start} must be int'
        raise BadStartException(msg)
    if y_start > max_dimens[1]:
        msg = f'Start at y value {y_start} not possible, {max_dimens[1]} max'
        raise OffMapException(msg)
    if cardinal not in ['N', 'E', 'S', 'W']:
        msg = f'Cardinal direction {cardinal} not valid'
        raise BadStartException(msg)


def validate_instructions(instruction_set: List) -> None:
    if type(instruction_set[0]) is not str:
        msg = f'{instruction_set} not valid instruction set'
        raise InvalidDirectionException(msg)
    for char in instruction_set[0]:
        if char not in ['L', 'R', 'M']:
            if char.isnumeric():
                continue
            else:
                msg = f'Direction set can accept only ints outside of L, R, M commands'
                raise InvalidDirectionException(msg)


def validate_planet(max_dimens: List[int]) -> None:
    if len(max_dimens) != 2:
        msg = f'Invalid dimension set passed for mars: {max_dimens} {len(max_dimens)} should be 2'
        raise InvalidPlanetDimensions(msg)
    if type(max_dimens[0]) is not int or type(max_dimens[1]) is not int:
        msg = f'Invalid values passed in for planet dimensions.  Must pass ints: {max_dimens}'
        raise InvalidPlanetDimensions(msg)

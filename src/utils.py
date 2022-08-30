import argparse
import csv
from enum import Enum
import sys
from typing import TextIO, Tuple
from src.validations import *


def read_input_file(rover_input: TextIO) -> Tuple[Tuple[int, int], List[Tuple[tuple, str]]]:
    rovers = []
    csv_reader = csv.reader(rover_input, delimiter=" ")

    try:
        max_dimens = [int(i) for i in next(csv_reader)]
        validate_planet(max_dimens)
    except InvalidPlanetDimensions as e:
        print(e)
        sys.exit()

    for row in csv_reader:
        try:
            validate_start(row, max_dimens)
            starting_location = int(row[0]), int(row[1]), row[2]
        except Exception as e:
            print(f'failed rover {e}')
            next(csv_reader)
            continue

        instructions = next(csv_reader)
        try:
            validate_instructions(instructions)
        except Exception as e:
            print(f'failed rover {e}')
            continue
        rovers.append((starting_location, instructions[0]))

    return tuple(max_dimens), rovers


def run_rover(start: Tuple[int, int, str],
              directions: str,
              max_dimens: Tuple[int, int]) -> Tuple[int, int, int]:

    present_position = (start[0], start[1])
    temp_orientation = CardinalDir[str(start[2])].value
    # print(f'presently at {present_position[0]}, {present_position[1]} facing {temp_orientation}')
    directions_list = enumerate(directions)
    for index, char in directions_list:
        print(f'presently at {present_position[0]}, {present_position[1]} facing {temp_orientation}')
        if 'R' == char:
            temp_orientation = (temp_orientation + 1) % 4
            print(f'Turning right')
            continue
        if 'L' == char:
            temp_orientation = (temp_orientation + 3) % 4
            print(f'Turning left')
            continue
        if 'M' == char:
            if index < (len(directions) - 1) and directions[index + 1].isnumeric():
                move_length = int(directions[index + 1])
                next(directions_list)
            else:
                move_length = 1
            print(f'Moving forward')
            if temp_orientation == 0:
                present_position = (present_position[0] + move_length, present_position[1])
                if present_position[0] > max_dimens[0]:
                    msg = f'Off the map! These directions take this rover off the flat planet mars'
                    raise OffMapException(msg)
            if temp_orientation == 1:
                present_position = (present_position[0], present_position[1] + move_length)
                if present_position[1] > max_dimens[1]:
                    msg = f'Off the map! These directions take this rover off the flat planet mars'
                    raise OffMapException(msg)
            if temp_orientation == 2:
                present_position = (present_position[0] - move_length, present_position[1])
                if present_position[0] < 0:
                    msg = f'Off the map! These directions take this rover off the flat planet mars'
                    raise OffMapException(msg)
            if temp_orientation == 3:
                present_position = (present_position[0], present_position[1] - move_length)
                if present_position[1] < 0:
                    msg = f'Off the map! These directions take this rover off the flat planet mars'
                    raise OffMapException(msg)
            continue
        else:
            raise InvalidDirectionException(f'Unrecognized character in direction set: {char}, {type(char)}')
    return present_position[0], present_position[1], temp_orientation


class CardinalDir(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

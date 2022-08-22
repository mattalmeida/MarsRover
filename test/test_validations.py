from src.validations import *
import pytest


def test_validate_start():
    start_pos = [1, 1, 'N']
    max_dims = [2, 2]
    assert validate_start(start_pos, max_dims) is None


def test_fail_validate_start_format():
    with pytest.raises(BadStartException):
        start_pos = [1, 1]
        max_dims = [2, 2]
        validate_start(start_pos, max_dims)


def test_fail_validate_start_args():
    with pytest.raises(BadStartException):
        start_pos = [1, 'c', 'N']
        max_dims = [2, 2]
        validate_start(start_pos, max_dims)


def test_fail_validate_start_off_map():
    with pytest.raises(OffMapException):
        start_pos = [2, 2, 'N']
        max_dims = [1, 1]
        validate_start(start_pos, max_dims)


def test_fail_validate_start_bad_card():
    with pytest.raises(BadStartException):
        start_pos = [2, 2, 'C']
        max_dims = [3, 3]
        validate_start(start_pos, max_dims)


def test_validate_instructions():
    instruction_set = ['LRLRM']
    assert validate_instructions(instruction_set) is None


def test_fail_validate_instructions_bad_type():
    with pytest.raises(InvalidDirectionException):
        instruction_set = [0]
        validate_instructions(instruction_set)


def test_fail_validate_instructions_bad_command():
    with pytest.raises(InvalidDirectionException):
        instruction_set = ['LS']
        validate_instructions(instruction_set)


def test_validate_planet():
    planet_size = [3, 3]
    assert validate_planet(planet_size) is None


def test_fail_validate_planet_bad_coord():
    with pytest.raises(InvalidPlanetDimensions):
        planet_size = [3]
        validate_planet(planet_size)


def test_fail_validate_planet_bad_type():
    with pytest.raises(InvalidPlanetDimensions):
        planet_size = ['one', 1]
        validate_planet(planet_size)

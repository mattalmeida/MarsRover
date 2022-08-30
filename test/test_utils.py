from src.utils import *
import pytest


# def test_read_input_file():
#     with open('test/test_input.csv', "r", newline='') as test_input:
#         max_dimens, rovers = read_input_file(test_input)
#         assert max_dimens[0] is 4
#         assert max_dimens[1] is 4
#         assert rovers[0][0][0] is 2
#         assert rovers[0][0][1] is 2
#         assert rovers[0][0][2] is 'N'
#         assert rovers[0][1] == 'LLM'
#         assert rovers[1][0][0] is 3
#         assert rovers[1][0][1] is 1
#         assert rovers[1][0][2] is 'W'
#         assert rovers[1][1] == 'MRM'
#
#
# def test_read_complex_input_file():
#     with open('test/test_complex_input.csv', "r", newline='') as test_input:
#         max_dimens, rovers = read_input_file(test_input)
#         assert max_dimens[0] is 4
#         assert max_dimens[1] is 4
#         assert rovers[0][0][0] is 2
#         assert rovers[0][0][1] is 2
#         assert rovers[0][0][2] is 'N'
#         assert rovers[0][1] == 'LLM2'
#
#
# def test_fail_bad_cardinal():
#     with pytest.raises(BadStartException):
#         with open('test/test_bad_cardinal.csv', "r", newline='') as test_input:
#             read_input_file(test_input)
#
#
# def test_fail_bad_format():
#     with pytest.raises(BadStartException):
#         with open('test/test_bad_format.csv', "r", newline='') as test_input:
#             read_input_file(test_input)
#
#
# def test_fail_bad_instruction():
#     with pytest.raises(InvalidDirectionException):
#         with open('test/test_bad_instruction.csv', "r", newline='') as test_input:
#             read_input_file(test_input)
#
#
# def test_run_rover():
#     start_pos = (0, 0, 'N')
#     directions = 'RMLM'
#     planet_size = (3, 3)
#     x, y, face = run_rover(start_pos, directions, planet_size)
#     assert x is 1
#     assert y is 1
#     assert face is 0


def test_run_complex_rover():
    start_pos = (0, 0, 'N')
    directions = 'RMLM3'
    planet_size = (3, 3)
    x, y, face = run_rover(start_pos, directions, planet_size)
    assert x is 1
    assert y is 3
    assert face is 0


# def test_fail_run_rover_off_map():
#     with pytest.raises(OffMapException):
#         start_pos = (0, 0, 'N')
#         directions = 'RMMLM'
#         planet_size = (1, 1)
#         run_rover(start_pos, directions, planet_size)

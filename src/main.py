from src.utils import *


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, help='Input file location', required=True)
    args = parser.parse_args()

    if args.file:
        with open(args.file, "r", newline='') as rover_input:
            max_dimens, rovers = read_input_file(rover_input)

    else:
        # TODO interactive mode input
        print(f'Must provide directory. \n\nusage: main.py [-h]')
        sys.exit()

    for rover in rovers:
        start = rover[0]
        directions = rover[1]

        try:
            outcome = run_rover(start, directions, max_dimens)
            print(f'{outcome[0]} {outcome[1]} {CardinalDir(outcome[2]).name}')
        except OffMapException as e:
            print(f'rover driven off map')
            continue


if __name__ == '__main__':
    main()

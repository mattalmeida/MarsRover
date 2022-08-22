## REQUIREMENTS
```
python >= 3.5
```

## TEST REQUIREMENTS
```
pytest
```

## Installation & Usage

To run the service, please execute the following from the projects root dir:

### Installation
```bash
# ensure you have at least Python 3.5
python -V

# install requirements (for tests)
pip install -r requirements.txt

# run service
python -m src.main --file <Input file location>
```

### Usage

```
required arguments:
  --file FILE       Input values file
```

### Example

```shell
python -m src.main --file example_input.csv
```
This command will grab the `example_input.csv` file to use as program input

### File format
The File format must look like
```
<int> int
<int> <int> <char>
<str>
```

The first line of input file is the upper-right coordinates of the plateau, the lower-left coordinates are assumed to be 0,0.

The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover's position, and the second line is a series of instructions telling the rover how to explore the plateau.

The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover's orientation.

Each rover will be finished sequentially, which means that the second rover won't start to move until the first one has finished moving.

### Testing
Tests can be run after installation with the following command:
```cmd
pytest
```
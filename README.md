# Strong admissibility labeling-based algorithms for SETAFs
This project provides an implementation of a generalization
toward SETAFs of labeling-based strong admissibility algorithms,
originally defined for ordinary argumentation frameworks (AFs),
as presented in
[Strong Admissibility, a Tractable Algorithmic Approach][caminada] by
Caminada and Harikrishnan.

[caminada]: https://research.wu.ac.at/files/26882780/paper3.pdf

## Execution
To run the project, Python 3 is required. `python -m strong-setaf` will display
a help message with a list of the possible subcommands that can be executed.
These commands are:

- `display-setaf`: reads a SETAF from a file in `.ccl` extension
    and displays it on screen. The following suboptions are accepted:
    - `--layout`: the layout with which the graph of the SETAF should be drawn;
- `display-sl`: short for "display strong labeling (SL)". Accepts a file in `.ccl` extension
    encoding a SETAF, computes a strongly admissible labeling for it and displays it on screen.
    The following suboptions are accepted:
  - `--layout`: the layout with which the graph of the SETAF should be drawn;
  - `--target`: a positive integer value representing an argument. Once the labeling
    algorithm assigns a positive (in) label to this argument, it stops and displays
    the graph on screen.

A small set of SETAFs in `.ccl` format is contained in the `data/` directory.

## Tests
The project includes a small unit test suite, written
using the `unittest` module of the Python standard
library.

To run it:

```bash
python3 -m unittest discover -v -p "*Test.py" test/
```
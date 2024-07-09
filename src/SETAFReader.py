from src.Attack import Attack
from src.SETAF import SETAF


class SETAFReader:
    def __init__(self, file):
        self._line_count = 0

        if type(file) is str:
            self._file = open(file, "tr")
        else:
            self._file = file

        self._arguments, self._attacks = self._read_first_line()

    def __call__(self):
        return SETAF(self._call_aux())

    def _call_aux(self):
        while self._line_count <= self._attacks:
            attacked, attackers = self._read_next_line()

            yield Attack(attackers, attacked)

    def _read_first_line(self):
        if self._line_count > 0:
            raise ValueError("First line can only be read once")

        self._line_count += 1

        arguments, attacks, zero = map(
            int, self._file.readline().split(" ")
        )

        if zero != 0:
            raise ValueError("A 0 is expected at the end of the line")

        if arguments < 0 or attacks < 0:
            raise ValueError("Number of arguments/attacks must be > 0")

        return arguments, attacks

    def _read_next_line(self):
        line = tuple(
            map(
                int, self._file.readline().split(" ")
            )
        )
        attacked = line[0]
        attackers = line[1:-1]
        self._line_count += 1

        if line[-1] != 0:
            raise ValueError("A 0 is expected at the end of the line")
        if not all(map(self._argument_is_valid, (attacked, ) + attackers)):
            raise ValueError(
                "Invalid argument found at line %d" % self._line_count
            )

        return attacked, attackers

    def _argument_is_valid(self, argument):
        return 1 <= argument <= self._arguments

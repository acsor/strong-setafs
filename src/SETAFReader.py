from src.Attack import Attack
from src.SETAF import SETAF


class SETAFReader:
    def __init__(self):
        pass

    def __call__(self, path):
        return SETAF(
            *self._call_aux(path)
        )

    @staticmethod
    def _call_aux(path):
        line_count = 0

        with open(path, "r") as file:
            for raw_line in file:
                line = tuple(
                    map(
                        int, raw_line.split(" ")
                    )
                )

                if line_count > 0:
                    if line[-1] != 0:
                        raise ValueError(
                            "A 0 is expected at the end of the line"
                        )

                yield Attack(line[0:-2], line[-2])

                line_count += 1

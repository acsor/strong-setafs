import enum
import random
from collections.abc import Iterable


class Label(enum.Enum):
    OUT = enum.auto()
    IN = enum.auto()
    UNDEC = enum.auto()


class SETAFLabeling:
    def __init__(self, setaf):
        self._setaf = setaf
        self._labels = dict()

    def __str__(self):
        return '\n'.join(
            '%s %s' % (a, self[a]) for a in self._setaf.arguments
        )

    def __getitem__(self, keys):
        if isinstance(keys, Iterable):
            values = frozenset(
                self._labels[k] for k in keys
            )

            return values if len(values) > 1 else tuple(values)[0]
        else:
            return self._labels[keys]

    def __setitem__(self, key, value):
        if value not in Label:
            raise ValueError("Label must be either IN, OUT or UNDEC")

        self._labels[key] = value

    def __iter__(self):
        return iter(self._labels)

    def keys(self):
        return self._labels.keys()

    @staticmethod
    def random_labeling(setaf):
        """
        :param setaf: A SETAF.
        :return: A SETAFLabeling instance mapping arguments and argument-attacks
        uniformly randomly to labels.
        """
        labels = SETAFLabeling(setaf)

        for a in setaf.attacks:
            labels[a.attacked] = random.choice(
                (Label.OUT, Label.IN, Label.UNDEC)
            )
            labels[a] = random.choice(
                (Label.OUT, Label.IN, Label.UNDEC)
            )

        return labels

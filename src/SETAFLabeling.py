import enum
import random


class Label(enum.Enum):
    OUT = enum.auto()
    IN = enum.auto()
    UNDEC = enum.auto()


class SETAFLabeling:
    def __init__(self, setaf):
        self._setaf = setaf
        self._labels = dict()

    def __getitem__(self, key):
        return self._labels[key]

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

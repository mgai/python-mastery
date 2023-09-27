from functools import total_ordering


@total_ordering
class MutInt:
    """A class to behave as if built-ins.
    @total_ordering will implement the missing comparison methods
    as long as __eq__ and one of other (__lt__) are implemented.
    """

    __slots__ = ["value"]

    def __init__(self, value):
        self.value = value

    # Fixing the output

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"MutInt({self.value})"

    def __format__(self, __format_spec: str) -> str:
        return format(self.value, __format_spec)

    # Math Operators

    def __add__(self, other):
        if isinstance(other, MutInt):
            return MutInt(self.value + other.value)
        elif isinstance(other, int):
            return MutInt(self.value + other)
        else:
            return NotImplemented

    __radd__ = __add__  # Reversed Add, so that 3+mutInt works.

    def __iadd__(self, other):
        """In-place add, +="""
        if isinstance(other, MutInt):
            self.value += other.value
            return self
        elif isinstance(other, int):
            self.value += other
            return self
        else:
            return NotImplemented

    # Comparisons

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, MutInt):
            return self.value == __value.value
        elif isinstance(__value, int):
            return self.value == __value
        else:
            return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MutInt):
            return self.value < other.value
        elif isinstance(other, int):
            return self.value < other
        else:
            return NotImplemented

    # Type converters - Python NEVER automatically converts data.

    def __int__(self):
        return self.value

    def __float__(self):
        return float(self.value)

    # Index Array[index]

    __index__ = __int__

"""Contains the necessary tools to generate a dataset."""

from dataclasses import dataclass


@dataclass(frozen=True)
class Hill:
    """The hill from which the jumpers fly off.
    
    The hill is located between 0 and `x_max`.

    .. code::

            |
            |     <- offset
            |\
            | \
            |  \
            --------------> x
                ^ x_max
    """

    offset: float
    """Vertical offset of slope - should be negative."""
    slope: float
    """Slope of the hill - should be negative."""
    x_max: float
    """Maximum extension of the hill - should be positive."""

    def y(self, x: float) -> float:
        """Returns shape of the hill."""
        return self.offset + self.slope * x

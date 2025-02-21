"""Contains the necessary tools to generate a dataset."""

from dataclasses import dataclass
import pathlib

EARTH_GRAVITY = 1.0
"""Acceleration on earth due to gravity."""


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


HILL = Hill(offset=-1.0, slope=-1.0, x_max=10.0)
"""The present hill."""


@dataclass(frozen=True)
class SkiJump:
    """The true jumping trajectory."""

    v0: float
    """Initial velocity."""
    alpha: float
    """Initial angle."""

    def y(self, x: float) -> float:
        """Return the trajectory."""
        raise NotImplementedError

    @classmethod
    def from_json_file(cls, path: pathlib.Path):
        """Read configuration from JSON file."""
        raise NotImplementedError()

    def landing(self, hill: Hill) -> float:
        """Returns the intersection of the trajectory and the hill."""
        raise NotImplementedError()

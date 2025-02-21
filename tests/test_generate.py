import sys

import numpy as np

sys.path.append("src/")
from generate import Hill


def test_hill():
    # check fixed configurations
    hill = Hill(offset=-1.0, slope=-1.0, x_max=10.0)
    np.testing.assert_allclose(hill.y(0.0), -1.0)
    np.testing.assert_allclose(hill.y(1.0), -2.0)

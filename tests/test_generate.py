import numpy as np
import sys

sys.path.append("src/")
from generate import Hill


def test_hill():
    # check fixed configurations
    hill1 = Hill(offset=-1.0, slope=-1.0, x_max=10.0)
    np.testing.assert_allclose(hill1.y(0.0), -1.0)
    np.testing.assert_allclose(hill1.y(1.0), -2.0)
    hill2 = Hill(offset=-1.5, slope=-2.0, x_max=10.0)
    np.testing.assert_allclose(hill2.y(0.0), -1.5)
    np.testing.assert_allclose(hill2.y(1.0), -3.5)

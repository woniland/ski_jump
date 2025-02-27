"""Contains the necessary tools to fit a dataset."""

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

# Step 1: Determine the starting velocity and starting angle of the test dataset `data/A-test.txt`.

## 1. Load data file using https://numpy.org/doc/stable/reference/generated/numpy.loadtxt.html#numpy-loadtxt .
##    The first column corresponds to the abscissa x and the second column to the ordinate y.

## 2. Define the model: Look to the example on SciPy (the link below)

## 3. Fit using https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#curve-fit

## 4. Calculate the initial velocity and initial angle.
##    (Yes, this is a math exercise ;-) )

# Step 2: Plot the data and your fit into one diagram.

## - Use e.g. https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.plot.html#matplotlib.pyplot.plot
## - Save the final plot in `plots/test.pdf`
## - Note it is often convenient to not commit generated files to repositories, but their recipe instead!

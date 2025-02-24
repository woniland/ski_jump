## Exercise A - Engineer

Your main task will to do the actual fitting, based on the datasets provided
by the Programmer.

### Fitting

We _assume_ the dataset describes a ski jump under the influence of gravity.
If we can setup a model, which reflects this assumption, and we can fit this model,
we can be confident that is was a normal ski jump after all.

**Step 1:** Determine the starting velocity and starting angle of the test dataset `data/test.txt`.

1. Read the input data from file
1. Define the model: $y(x;a,b) = a*x + b*x^2$ (as you know: with gravity object fly like parabolas)
1. Fit the model parameters $a,b$ to the data using
   [scipy.optimize.curve_fit](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#curve-fit)
1. Find the transformation from $a,b$ to the initial velocity and initial angle

### Plotting

Next, we want to check if the fit actually makes sense.

**Step 2:** Plot the data and your fit into one diagram.

_Hint:_ Recall that the data points are just points, but the model is a smooth function.

For a small number of model parameters it often makes sense to print them in the plot.

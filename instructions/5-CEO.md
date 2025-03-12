## Exercise C - CEO

### Issues

**Step 1:** Open Issues for the various groups if you think that was useful.

### Packaging

Python provides an easy way to bundle and distribute libraries and also associated scripts:
building actual Python packages.

First, you should turn the `src/` folder into an actual module by adding an empty file
called `__init__.py`. 
To learn more about modules you can read, e.g., [the online documentation](https://docs.python.org/3/tutorial/modules.html).

Next, we want to setup the Python package: this can be achieved by writing a `pyproject.toml` file.
Read the online documentation on how to create this file: https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

**Step 2:** Write a `pyproject.toml` file.

By convention the source files of the package are in `src/<your-package>/`, i.e. you should move the current files
in `src/` one directory down with the name that you choose for your package.

You can read more about the general idea of packaging online: https://packaging.python.org/en/latest/tutorials/packaging-projects/

## Exercise A - Programmer

Your main task will be to provide the dataset - i.e. the starting point for the Engineer.
We will do so by inventing our own universe in which we dictate the laws of physics.
By chance, the laws will be similar to our own universe, but we will not tell this
fact to the engineer. In order to generate these dataset we develop a set of tools,
which we can then execute.

### Implementation

You will start to work on the `src/generate.py` file - take a look there!

### Unit testing

Next, we want to check if the implementation is actually correct - we can do this
by using the concept of [Unit testing](https://en.wikipedia.org/wiki/Unit_testing).
Unit test execute a small piece of code in fully controlled environment and check if it
fulfills the expectations.

- If a code does not pass the unit tests there is no hope it will work in real life
- Unit tests should be a small, independent piece of logic
- Unit tests should be executed regularly, e.g. on every commit
- Unit tests often check invariants or symmetries of your code

The most popular unit test framework for Python is [pytest](https://docs.pytest.org/en/stable/).

Take a look to the `tests/test_generate.py` file!
By convention unit test files start with `test_`and also unit test functions start with `test_`.

Install the package via
```sh
$ pip install pytest
```
Execute the already available unit test via
```sh
$ pytest tests/
```

### Data generation

Finally, we have all tools at hand to write the actual datafile.
To execute the generation script execute
```sh
$ python src/generate.py
```

### Action plan

1. Complete the implementation for the `SkiJump` class.
1. Check your implementation using the available unit tests and write the missing ones.
1. Complete the dataset generation script in `src/generate.py`.

_Hint_: It often makes sense to do Step 1 & 2 in parallel.
This way it could e.g. make sense to just put the implementation of the trajectory into one branch.

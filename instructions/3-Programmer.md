## Exercise A - Programmer

Your main task will be to provide the dataset - i.e. the starting point for the Engineer.
We will do so by inventing our own universe in which we dictate the laws of physics.
In order to generate these dataset we develop a set of tools,
which we can then execute.

_Hint_: It often makes sense to do the implementation (Step 1) and the unit test (Step 2) in parallel.
This way it could, e.g., make sense to just put the implementation of the trajectory
and its associated unit tests into one branch.

You will work on the `src/generate.py` file - take a look there!

### Implementation

**Step 1:** Complete the implementation of `SkiJump.y`, `SkiJump.from_json_file`,
and `SkiJump.landing`.

_Hints:_
- for `SkiJump.y`: it is $y(x) = a*x + b*x^2$ - determine $a,b$ from the
  initial velocity and angle! (Yes, this is a math exercise :books: )
- for `SkiJump.from_json_file`: use [`json.load`](https://docs.python.org/3/library/json.html#json.load)
- for `SkiJump.landing`: More math!

We will leave `SkiJump.sample` for step 3.

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

**Step 2:** Check your implementation using the available unit tests and write the missing ones.

### Data generation

Finally, we have all tools at hand to write the actual datafile.
To execute the generation script execute
```sh
$ python src/generate.py
```

**Step 3:** Complete the implementation of `SkiJump.sample` and the dataset generation script in `src/generate.py`.

Check that `config/A-test.json` reproduces `data/A-test.txt` when running
```sh
$ python src/generate.py config/A-test.json data/A-test.txt -n 3
```

Generate some new theories (in `config/`), then generate a new dataset (from that), and then put them into
the `data/` folder for the Engineer.

## Exercise A - CEO

Your main task will be to organize the repository.

### Pull Requests and Issues

Make sure that all three teams use Pull Request to implement new features and that a suitable reviewer is assigned.
For every Pull Request check that the contribution
- makes sense, i.e. is physically correct
- does not contain trivial typos
- is sufficiently documented

**Step 1**: Open three Issues to track the status of the three groups in Exercise A.

It often makes sense to annotate the respective Pull Request behind a completed task,
e.g. `- [ ] task 1` -> `- [x] task 1 #2`.

#### CEO Issue

Title: `A/CEO`
Assignees: the CEO group
Description:
```
- [ ] open all issues for exercise A
- [ ] enforce code formatting via pre-commit
- [ ] add CI with unit tests
```

#### Programmer Issue

Title: `A/Programmer`
Assignees: the Programmer group
Description:
```
- [ ] complete `SkiJump`
- [ ] unit test all methods
- [ ] data generation
```

#### Engineer Issue

Title: `A/Engineer`
Assignees: the Engineer group
Description:
```
- [ ] can fit template data
- [ ] plot fit comparing to data
```

### Code formatting

When writing larger pieces of code (meaning >50 lines) or when developing codes together in a
collaboration code formatting is becoming an issue.

For example, this is allowed Python code
```py
def f(a   = .1, b=0.):
    return a  +b
f(
1.,     3.)
```
but arguably much harder to read then
```py
def f(a=0.1, b=0.0):
    return a + b


f(1.0, 3.0)
```

Let's use _the same_ formatting everywhere - we can do this by
using the popular [black](https://github.com/psf/black) program.

Now, just using `black` on its own would require everybody to run it constantly - but people might forget it
and we are back to square one, with all mixed code formatting.

Instead, we can _enforce_ the running of `black` by making it run _before every commit_, i.e. before anyone can
contribute to the repository. We can do so by using the [hooks](https://git-scm.com/book/ms/v2/Customizing-Git-Git-Hooks)
which `git` provides and specifically there is a convenient python library for precisely that purpose:
[pre-commit](https://pre-commit.com/).

**Step 2**: Add a pre-commit configuration using the [Quick Start instructions](https://pre-commit.com/#installation) which
should include (at least) the standard white-space hooks and black.

Implement this feature through a Pull Request and tell your collaborators this way what they should do and how they can activate
it on their machines.

# python-build ![checks](https://github.com/FFY00/python-build/workflows/checks/badge.svg) ![tests](https://github.com/FFY00/python-build/workflows/tests/badge.svg) [![codecov](https://codecov.io/gh/FFY00/python-build/branch/master/graph/badge.svg)](https://codecov.io/gh/FFY00/python-build) [![Documentation Status](https://readthedocs.org/projects/python-build/badge/?version=latest)](https://python-build.readthedocs.io/en/latest/?badge=latest) [![PyPI version](https://badge.fury.io/py/build.svg)](https://pypi.org/project/build/)

A simple, correct PEP517 package builder.

```sh
$ python -m build -h
usage: python -m build [-h] [--sdist] [--wheel] [--outdir ./dist] [--skip-dependencies] [.]

positional arguments:
  .                     source directory (defaults to current directory)

optional arguments:
  -h, --help            show this help message and exit
  --sdist, -s           build a source package
  --wheel, -w           build a wheel
  --outdir ./dist, -o ./dist
                        output directory
  --skip-dependencies, -x
                        does not check for the dependencies
  --no-isolation, -n    do not isolate the build in a virtual environment (requires build dependencies to be present)
```

See the [documentation](https://python-build.readthedocs.io/en/latest/) for more information.

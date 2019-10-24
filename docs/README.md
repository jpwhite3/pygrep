PyGrep
--------

Let's create a simple tool that will allow us to search through text files for a given regular expression pattern, inspired by the classic unix `grep` tool.

# Simple script

```bash
touch pygrep.py     # Create a text file called pygrep.py
```

```python
import re
import sys


def regex_search(expression, target_string, ignorecase=False):
    raw_expression = re.escape(expression)
    if ignorecase:
        return re.search(raw_expression, target_string, re.I)
    return re.search(raw_expression, target_string)


def grep(expression, filepath, ignorecase=False):
    results = []
    with open(filepath) as file:
        for line_no, line in enumerate(file):
            if regex_search(expression, line, ignorecase):
                current_line_info = (filepath, line_no, line)
                results.append(current_line_info)
    return results


expression = sys.argv[1]
filepath = sys.argv[2]
results = grep(expression, filepath)
print(results)
```

# Reusable module

Let's refactor the last few lines of the code above so that this code is more reusable.

```python
# https://docs.python.org/3/library/__main__.html
if __name__ == '__main__':
    expression = sys.argv[1]
    filepath = sys.argv[2]
    results = grep(expression, filepath)
    print(results)
```

# Add a proper CLI

Right now, a person has to read the code to be able to use it... not very user friendly. Let's fix that by adding a proper CLI - with inline help and more readable output.

```python
import argparse

# [include all code from above]

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('expression', action='store', type=str, help='Regex to search for')
    parser.add_argument('filepath', action='store', type=str, help='Text file to search through')
    args = parser.parse_args()

    results = grep(args.expression, args.filepath)
    for result in results:
        output = "[%s] [%s] %s" % result
        print(output.strip("\n"))
```

# Refactor into a package

```bash
mkdir pygrep
mv pygrep.py pygrep/__init__.py

python -m pygrep
```
It fails, complaining about a missing module named __main__ and that the package can't be executed. Let's make that work by moving some code around. We are going to moe the code from within that `if __name__ == '__main__'` section into a new file.

```bash
touch pygrep/__main__.py
```

```python
import argparse
from . import grep

parser = argparse.ArgumentParser()
parser.add_argument('expression', action='store', type=str, help='Regex to search for')
parser.add_argument('filepath', action='store', type=str, help='Text file to search through')
args = parser.parse_args()

results = grep(args.expression, args.filepath)
for result in results:
    output = "[%s] [%s] %s" % result
    print(output.strip("\n"))
```

```bash
python -m pygrep -h
```

# Add some tests now

```bash
mkdir tests
touch tests/__init__.py
touch tests/test_pygrep.py
touch tests/TestFixture.txt
```

```python
from unittest import TestCase
import os
import pygrep

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURE = os.path.join(BASE_DIR, "TestFixture.txt")


class TestGrep(TestCase):
    def test_honorcase(self):
        results = pygrep.grep("test", FIXTURE)
        expected = 1
        actual = len(results)
        self.assertEqual(expected, actual)
```

```bash
python -m unittest discover
```

# Prep for distribution

```bash
touch setup.py
touch setup.cfg
```

**setup.py**
```python
from setuptools import setup

setup(
    name="pygrep",
    version="0.1.0",
    description="A pure Python implementation of GREP",
    packages=["pygrep"],
    include_package_data=True,
    zip_safe=False,
)
```

**setup.cfg**
```
[bdist_wheel]
universal=1
```

This flag says that the code is written to work on both Python 2 and Python 3. If at all possible, it is good practice to do this. If you cannot, you will need to generate wheels for each Python version that you support.

```bash
python setup.py sdist
python setup.py bdist_wheel
```
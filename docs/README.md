PyGrep
--------

Let's create a simple tool that will allow us to search through text files for a given regular expression pattern, inspired by the classic unix `grep` tool.

# Simple script

```bash
touch pygreg.py     # Create a text file called pygrep.py
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
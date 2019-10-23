import sys
import re


def eprint(*args, **kwargs):
    # Print to STDERR instead of STDOUT
    print(*args, file=sys.stderr, **kwargs)


def grep(expression, filepath, ignorecase=False, invert=False):
    results = []
    raw_expression = re.escape(expression)
    with open(filepath) as file:
        line_number = 0
        for line in file:
            line_number += 1
            # Enable case matching?
            if ignorecase:
                matches = re.search(raw_expression, line, re.I)
            else:
                matches = re.search(raw_expression, line)

            # Invert matches if need be and print
            if matches and not invert:
                results.append(line)
            elif invert and not matches:
                results.append(line)
    return results

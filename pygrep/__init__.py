import sys
import re


def eprint(*args, **kwargs):
    # Print to STDERR instead of STDOUT
    print(*args, file=sys.stderr, **kwargs)


def regex_search(expression, target_string, ignorecase=False):
    raw_expression = re.escape(expression)
    if ignorecase:
        return re.search(raw_expression, target_string, re.I)
    return re.search(raw_expression, target_string)


def grep(expression, filepath, ignorecase=False, invert=False):
    results = []
    with open(filepath) as file:
        line_number = 0
        for line in file:
            line_number += 1
            matches = regex_search(expression, line, ignorecase)

            # Invert matches if need be and print
            current_line_info = (filepath, line_number, line)
            if matches and not invert:
                results.append(current_line_info)
            elif invert and not matches:
                results.append(current_line_info)
    return results

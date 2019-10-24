import re


def regex_search(expression, target_string, ignorecase=False):
    raw_expression = re.escape(expression)
    if ignorecase:
        return re.search(raw_expression, target_string, re.I)
    return re.search(raw_expression, target_string)


def grep(expression, filepath, ignorecase=False, invert=False):
    results = []
    with open(filepath) as file:
        for line_no, line in enumerate(file):
            matches = regex_search(expression, line, ignorecase)

            # Invert matches if need be and print
            current_line_info = (filepath, line_no, line)
            if matches and not invert:
                results.append(current_line_info)
            elif invert and not matches:
                results.append(current_line_info)
    return results

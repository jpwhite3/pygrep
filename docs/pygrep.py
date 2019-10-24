import re
import sys
import argparse


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


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('expression', action='store',
                        type=str, help='Regex to search for')
    parser.add_argument('filepath', action='store', type=str,
                        help='Text file to search through')
    args = parser.parse_args()

    results = grep(args.expression, args.filepath)
    for result in results:
        output = "[%s] [%s] %s" % result
        print(output.strip("\n"))

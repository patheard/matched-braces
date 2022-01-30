"Module that checks if a given string has balanced braces"

import re


def is_balanced(input_str):
    "Check if the input string has balanced braces"

    valid_braces = {"{": "}", "[": "]", "(": ")"}

    # Remove all non-brace characters
    only_braces = re.compile("[^\\[\\]\\{\\}\\(\\)]")
    brace_string = only_braces.sub("", input_str)

    # Valid brace string must be even length
    if len(brace_string) % 2 != 0 or len(brace_string) == 0:
        return False

    # Check if the string is balanced
    stack = []
    for char in brace_string:
        if char in ["[", "{", "("]:
            stack.append(char)
        else:
            brace = stack.pop()
            if valid_braces[brace] != char:
                return False

    return True

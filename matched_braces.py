"Module that checks if a given string has matching braces"

import re


def match_braces(input_str):
    "Check if the input string has matching braces"

    # Remove all non-brace characters
    only_braces = re.compile("[^\\[\\]\\{\\}\\(\\)]")
    brace_string = only_braces.sub("", input_str)

    # Valid brace string must be even length
    if len(brace_string) % 2 != 0:
        return False

    # Check if the string is balanced
    stack = []
    for char in brace_string:
        if char in ["[", "{", "("]:
            stack.append(char)
        else:
            if len(stack) == 0:
                return False
            if char == "]" and stack[-1] != "[":
                return False
            if char == "}" and stack[-1] != "{":
                return False
            if char == ")" and stack[-1] != "(":
                return False
            stack.pop()

    return True

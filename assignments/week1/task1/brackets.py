# python3

import sys


class Bracket:
    def __init__(self, bracket_type, position):
        self.bracket_type = bracket_type
        self.position = position

    def Match(self, c):
        if self.bracket_type == "[" and c == "]":
            return True
        if self.bracket_type == "{" and c == "}":
            return True
        if self.bracket_type == "(" and c == ")":
            return True
        return False


if __name__ == "__main__":
    text = sys.stdin.read()

    opening_brackets = []
    for i, next in enumerate(text, start=1):
        if next == "(" or next == "[" or next == "{":
            # Process opening bracket
            opening_brackets.append(Bracket(next, i))

        if next == ")" or next == "]" or next == "}":
            # Process closing bracket
            if not opening_brackets or not opening_brackets[-1].Match(next):
                print(i)
                exit(0)
            opening_brackets.pop()

    if opening_brackets:
        print(opening_brackets[0].position)
    else:
        print("Success")

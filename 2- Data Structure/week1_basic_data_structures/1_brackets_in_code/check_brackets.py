# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            if opening_brackets_stack == []:
                return i + 1

            if not (are_matching(opening_brackets_stack.pop().char, next)):
                return i+1
            
    if opening_brackets_stack == []:
        return "Success"
    else:
        return opening_brackets_stack[-1].position
    

def main():
    text = input()
    print(find_mismatch(text))



if __name__ == "__main__":
    main()

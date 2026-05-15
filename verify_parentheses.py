input_string = input("Enter a string: ")

open_parentheses = "([{"
close_parentheses = ")]}"

stack = []

for char in input_string:
    if char in open_parentheses:
        stack.append(char)
    elif char in close_parentheses:
        if not stack:
            print("Unbalanced")
            exit()
        top = stack.pop()
        if open_parentheses.index(top) != close_parentheses.index(char):
            print("Unbalanced")
            exit()

if stack:
    print("Unbalanced")
else:
    print("Balanced")
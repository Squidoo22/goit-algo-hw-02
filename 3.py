def check_brackets(expression):
    bracket_pairs = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    stack = []

    for char in expression:
        if char in bracket_pairs:
            stack.append(char)
        elif char in bracket_pairs.values():
            if stack and bracket_pairs[stack[-1]] == char:
                stack.pop()
            else:
                return "Несиметрично"

    return "Симетрично" if not stack else "Несиметрично"


expressions = [
    "( ){[ 1 ]( 1 + 3 )( ){ }}",
    "( 23 ( 2 - 3);",
    "( 11 }"
]

for expr in expressions:
    print(f"{expr}: {check_brackets(expr)}")

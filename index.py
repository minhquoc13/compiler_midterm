import re

# Define regular expressions for tokens
patterns = [
    ('keyword', r'\b(void|int|for|while|if|else|return|break|continue|float|void)\b'),
    ('identifier', r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ('num', r'\b\d+(\.\d+)?(E[+-]?\d+)?\b'),
    ('addop', r'[+\-]'),
    ('mulop', r'[\*/]'),
    ('relop', r'[<>]=?|==|!='),
    ('and', r'&&'),
    ('or', r'\|\|'),
    ('not', r'!'),
    ('(', r'\)'),
    ('(', r'\('),
    ('{', r'\{'),
    ('}', r'\}'),
    ('[', r'\['),
    (']', r'\]'),
    ('whitespace', r'[\s\n]+'),  # Pattern for space and newline
]

# Read the input file
with open('input.txt', 'r') as file:
    code = file.read()

tokens = []

errors = []

# Tokenize the code
while code:
    matched = False
    for token_type, pattern in patterns:
        match = re.match(pattern, code)
        if match:
            token = match.group(0)
            tokens.append((token_type, token))
            code = code[len(token):]
            matched = True
            break

    if not matched:
        # If no pattern matches, there's an unrecognized character
        print(f'Error: {code[0]}')
        errors.append(('Error', code[0]))
        code = code[1:]

# Print the list of tokens
for token_type, token in tokens:
    if (token_type != 'whitespace'):
        print(f'{token_type} : {token}')

for error_type, error_char in errors:
    print(f'{error_type} : {error_char}')

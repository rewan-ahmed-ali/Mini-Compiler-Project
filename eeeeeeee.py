import re

def parse_file(filename):
    try:
        with open(filename, 'r') as file:
            code = file.read()
            tokens = tokenize(code)
            parse(tokens)
    except FileNotFoundError:
        print("File not found!")

def tokenize(code):
    # Tokenize the input code
    tokens = re.findall(r'\bint\b|\bif\b|\bprint\b|[a-zA-Z_]\w*|[=><()+-]|[{};]', code)
    return tokens

def parse(tokens):
    try:
        # Start parsing
        pos = 0
        while pos < len(tokens):
            token = tokens[pos]
            if token == 'int':
                pos = parse_declaration(tokens, pos)
            elif token == 'if':
                pos = parse_conditional(tokens, pos)
            elif token == 'print':
                pos = parse_print(tokens, pos)
            elif token == ';':
                pos += 1
            else:
                raise SyntaxError("Unexpected token '{}'".format(token))
    except SyntaxError as e:
        print("Syntax Error:", e)

def parse_declaration(tokens, pos):
    var_name = tokens[pos + 1]
    if tokens[pos + 2] == '=':
        value = tokens[pos + 3]
        if tokens[pos + 4] != ';':
            raise SyntaxError("Expected ';' after variable declaration")
        print("Variable '{}' declared with value '{}'".format(var_name, value))
        return pos + 5
    elif tokens[pos + 2] == ';':
        print("Variable '{}' declared without initialization".format(var_name))
        return pos + 3
    else:
        raise SyntaxError("Invalid variable declaration")

def parse_conditional(tokens, pos):
    if tokens[pos + 1] == '(' and tokens[pos + 5] == ')' and tokens[pos + 6] == '{' and tokens[pos + 8] == '}':
        condition = " ".join(tokens[pos + 2:pos + 5])
        print("Conditional statement with condition:", condition)
        return pos + 9
    else:
        raise SyntaxError("Invalid conditional statement")

def parse_print(tokens, pos):
    if tokens[pos + 1] == '(' and tokens[pos + 2] != ')' and tokens[pos + 3] == ')' and tokens[pos + 4] == ';':
        variable = tokens[pos + 2]
        print("Print statement with variable:", variable)
        return pos + 5
    else:
        raise SyntaxError("Invalid print statement")

# Example usage
parse_file("error.txt")

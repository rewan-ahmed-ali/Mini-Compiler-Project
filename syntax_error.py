# phase2 syntax_error
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
    tokens = re.findall(r'\bint\b|\bif\b|\bprint\b|[a-z_]\w*|[=><()+-]|[{};]', code)
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
                raise SyntaxError("Unexpected int before identifier'{}'".format(token))
    except SyntaxError as e:
        print("Syntax Error:", e)

def parse_declaration(tokens, pos):
    try:
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
    except IndexError:
        raise SyntaxError("Incomplete variable declaration")

def parse_conditional(tokens, pos):
    try:
        if tokens[pos + 1] == '(' and tokens[pos + 4] == ')' and tokens[pos + 6] == '{' and tokens[pos + 8] == '}' and tokens[pos + 9] == ';':
            condition = " ".join(tokens[pos + 2:pos + 5])
            print("Conditional statement with condition:", condition)
            return pos + 10
        else:
            raise SyntaxError("Invalid conditional statement")
    except IndexError:
        raise SyntaxError("Incomplete conditional statement")

def parse_print(tokens, pos):
    try:
        if tokens[pos + 1] == '(' and tokens[pos + 4] == ')' and tokens[pos + 5] == ';' and tokens[pos + 6] == ';':
            variable = tokens[pos + 3]
            print("Print statement with variable:", variable)
            return pos + 7
        else:
            raise SyntaxError("Invalid print statement")
    except IndexError:
        raise SyntaxError("Incomplete print statement")

try:
    parse_file("error.txt")
except SyntaxError as e:
    print("Syntax Error:", e)
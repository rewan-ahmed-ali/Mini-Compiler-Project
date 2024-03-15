# if_stmt ::= "if" expression ":" suite
# <expression> ::= <number>
#               | <expression> + <expression>
#               | <expression> - <expression> 
#               | <expression> * <expression> 
#               | <expression> / <expression> 


# if_stmt ::= "if" condition ":" suite
# assignment_stmt ::= identifier "+" identifier "=" expression

# identifier ::= [a-zA-Z_][a-zA-Z0-9_]*
# expression ::= term | expression "+" term | expression "-" term
# term ::= factor | term "*" factor | term "/" factor
# factor ::= identifier | literal | "(" expression ")"
# literal ::= [0-9]+

import re

def tokenize(code):
    return re.findall(r'\d+|\+|-', code) 

def parse(tokens):
    token = tokens.pop(0)
    
    if token == '+':
        return ['+', parse(tokens), parse(tokens)]
    elif token == '-':
        return ['-', parse(tokens), parse(tokens)]
    elif token.isdigit():
        return ['INT', int(token)] 
    
def generate(ast):
    if ast[0] == 'INT':
        return [f"PUSH {ast[1]}"]
    else:
        left_code = generate(ast[1])
        right_code = generate(ast[2])
        if ast[0] == '+':
            return left_code + right_code + ["ADD"]
        elif ast[0] == '-':
            return left_code + right_code + ["SUB"] 
        
def compile(code):
    tokens = tokenize(code)
    ast = parse(tokens)
    return generate(ast) 
code = "+ 5 - 3 2"
print("\n".join(compile(code)))


# statement ::= assignment_stmt
#             | declaration_stmt
#             | loop_stmt
#             | if_stmt

# assignment_stmt ::= identifier "=" expression

# declaration_stmt ::= "int" identifier "=" number

# loop_stmt ::= "for" identifier "in" "range" ":" suite

# if_stmt ::= "if" condition ":" suite

# expression ::= identifier
#               | number
#               | <expression> + <expression>
#               | <expression> - <expression> 
#               | <expression> * <expression> 
#               | <expression> / <expression> 

# condition ::= identifier comparison_operator number

# comparison_operator ::= ">" | "<" | ">=" | "<=" | "==" | "!="

# identifier ::= [a-zA-Z_][a-zA-Z0-9_]*

# number ::= [0-9]+

# suite ::= statement


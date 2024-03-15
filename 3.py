# # if_stmt ::= "if" expression ":" suite
# # <expression> ::= <number>
# #               | <expression> + <expression>
# #               | <expression> - <expression> 
# #               | <expression> * <expression> 
# #               | <expression> / <expression> 


# # if_stmt ::= "if" condition ":" suite
# # assignment_stmt ::= identifier "+" identifier "=" expression

# # identifier ::= [a-zA-Z_][a-zA-Z0-9_]*
# # expression ::= term | expression "+" term | expression "-" term
# # term ::= factor | term "*" factor | term "/" factor
# # factor ::= identifier | literal | "(" expression ")"
# # literal ::= [0-9]+

# import re

# def tokenize(code):
#     return re.findall(r'\d+|\+|-', code) 

# def parse(tokens):
#     token = tokens.pop(0)
    
#     if token == '+':
#         return ['+', parse(tokens), parse(tokens)]
#     elif token == '-':
#         return ['-', parse(tokens), parse(tokens)]
#     elif token.isdigit():
#         return ['INT', int(token)] 
    
# def generate(ast):
#     if ast[0] == 'INT':
#         return [f"PUSH {ast[1]}"]
#     else:
#         left_code = generate(ast[1])
#         right_code = generate(ast[2])
#         if ast[0] == '+':
#             return left_code + right_code + ["ADD"]
#         elif ast[0] == '-':
#             return left_code + right_code + ["SUB"] 
        
# def compile(code):
#     tokens = tokenize(code)
#     ast = parse(tokens)
#     return generate(ast) 
# code = "+ 5 - 3 2"
# print("\n".join(compile(code)))


# # statement ::= assignment_stmt
# #             | declaration_stmt
# #             | loop_stmt
# #             | if_stmt

# # assignment_stmt ::= identifier "=" expression

# # declaration_stmt ::= "int" identifier "=" number

# # loop_stmt ::= "for" identifier "in" "range" ":" suite

# # if_stmt ::= "if" condition ":" suite

# # expression ::= identifier
# #               | number
# #               | <expression> + <expression>
# #               | <expression> - <expression> 
# #               | <expression> * <expression> 
# #               | <expression> / <expression> 

# # condition ::= identifier comparison_operator number

# # comparison_operator ::= ">" | "<" | ">=" | "<=" | "==" | "!="

# # identifier ::= [a-zA-Z_][a-zA-Z0-9_]*

# # number ::= [0-9]+

# # suite ::= statement

import re

# Open the text file for reading
with open('text.txt', 'r') as file:
    # Read the entire contents of the file
    file_contents = file.read()

# Split the text into words and operators using regular expressions
split_text = re.findall(r'\b\w+\b|[^\w\s]', file_contents)

# Define a function to determine the token for a lexeme
def determine_token(lexeme):
    if lexeme.isnumeric():
        return "NUMBER"
    elif lexeme in ["for", "while", "if", "else"]:
        return lexeme.upper()  # Return the keyword as token in uppercase
    elif lexeme.isalpha():
        return "IDENTIFIER"
    else:
        return "OPERATOR"

# Create dictionaries to store the counts of tokens and lexemes
token_counts = {}
lexeme_counts = {}

# Iterate over the split text
for lexeme in split_text:
    token = determine_token(lexeme)
    
    # Update token count
    token_counts[token] = token_counts.get(token, 0) + 1
    
    # Update lexeme count
    lexeme_counts[lexeme] = lexeme_counts.get(lexeme, 0) + 1

# Print the token-lexeme pairs with lexemes in one column and tokens in the other
print("LEXEME          TOKEN        COUNT")
for lexeme, token in zip(split_text, map(determine_token, split_text)):
    print(f"{lexeme:<15} {token:<12} {lexeme_counts[lexeme]:<5}")

# Print token counts
print("\nToken Counts:")
for token, count in token_counts.items():
    print(f"{token}: {count}")

# Print lexeme counts
print("\nLexeme Counts:")
for lexeme, count in lexeme_counts.items():
    print(f"{lexeme}: {count}")

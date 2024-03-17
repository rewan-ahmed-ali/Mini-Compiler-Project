import re

# Read the contents of the text file
with open('text.txt', 'r') as file:
    file_contents = file.read()

# Split the text into words and operators using regular expressions
split_text = re.findall(r'\b\w+\b|[^\w\s]', file_contents)


def determine_token(lexeme):
    if lexeme.isnumeric():
        return "NUMBER"
    elif lexeme in ["for", "while", "if", "else"]:
        return lexeme.upper()
    elif lexeme in ["in","print","range"]:
        return "KEYWORD"
    elif lexeme.isalpha():
        return "IDENTIFIER"
    elif lexeme in ["(",")"]:
        return "PARENTHESIS"
    else:
        return "OPERATOR"


# token and lexeme counts
token_lexeme_pairs = []
token_counts = {}
print("LEXEME          TOKEN")

for lexeme in split_text:
    token = determine_token(lexeme)
    print(f"{lexeme:<15} {token}")

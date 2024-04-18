import re

with open('text.txt', 'r') as file:
    file_contents = file.read()


split_text = re.findall(r'\b\w+\b|[^\w\s]', file_contents)

def determine_token(lexeme):
    if lexeme.isnumeric():
        return "NUMBER"
    elif lexeme in ["for", "while", "if", "else"]:
        return lexeme.upper()
    elif lexeme in ["in","print","range","int","float"]:
        return "KEYWORD"
    elif lexeme.isalpha():
        return "IDENTIFIER"
    elif lexeme in ["(",")","}","{"]:
        return "PARENTHESIS"
    elif lexeme in [";"]:
        return "SYMBOL"
    else:
        return "OPERATOR"


# token and lexeme counts
token_lexeme_pairs = []
token_counts = {}
print("LEXEME          TOKEN")
for lexeme in split_text:
    token = determine_token(lexeme)
    token_lexeme_pairs.append((token, lexeme))  # Save token-lexeme pair
    token_counts[token] = token_counts.get(token, 0) + 1
    print(f"{lexeme:<15} {token}")

# Save tokens and lexemes to a new file
with open('tokens_and_lexemes.txt', 'w') as output_file:
    for token, lexeme in token_lexeme_pairs:
        output_file.write(f"{token:<23}\t{lexeme}\n")


total_tokens = sum(token_counts.values())
print(f"\nTotal number of Tokens: {total_tokens}")


print("\nToken Counts:")
for token, count in token_counts.items():
    print(f"{token}: {count}")

# grammar rules
grammar_rules = {
    "S": ["Statement"],
    "Statement": ["Assignment", "Conditional", "PrintStatement"],
    "Assignment": ["Type identifier '=' Value ';'"],
    "Type": ["'int'", "'float'"],
    "identifier": ["'a'", "'b'", "'c'", "'x'", "'y'", "'z'", "'r'"],
    "Value": ["NUMBER", "FLOAT"],
    "NUMBER": ["DIGIT", "DIGIT DIGITS"],
    "FLOAT": ["DIGIT '.' DIGIT", "DIGIT DIGITS '.' DIGIT", "DIGIT '.' DIGITS", "DIGIT DIGITS '.' DIGITS"],
    "DIGIT": ["'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'"],
    "DIGITS": ["DIGIT", "DIGIT DIGITS"],
    "Conditional": ["'if' '(' Condition ')' '{' Statement '}'"],
    "Condition": ["identifier '>' NUMBER"],
    "PrintStatement": ["'print' '(' identifier ')' ';'"]

}

print("\nGrammar Table:")
print("\nRule\t\t\tComponents")
for rule, components in grammar_rules.items():
    print(f"{rule:<23} {', '.join(components)}")

# regular expressions
regex_patterns = {
    "Assignment": r"(int|float)\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(\d+|\d+\.\d+)\s*;",
    "Conditional": r"if\s*\(\s*[a-zA-Z_][a-zA-Z0-9_]*\s*>\s*\d+\s*\)\s*\{\s*Statement\s*\}",
    "PrintStatement": r"print\s*\(\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\)\s*;",
    "identifier": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "NUMBER": r"\d+|\d+\.\d+"
}


# print("\nRegular Expressions:")
# for rule, pattern in regex_patterns.items():
#     print(f"{rule}: {pattern}")
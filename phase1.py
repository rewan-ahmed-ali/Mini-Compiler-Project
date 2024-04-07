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
    elif lexeme in ["in","print","range","int"]:
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
    # Update token count
    token_counts[token] = token_counts.get(token, 0) + 1
    print(f"{lexeme:<15} {token}")

# Save tokens and lexemes to a new file
with open('tokens_and_lexemes.txt', 'w') as output_file:
    for token, lexeme in token_lexeme_pairs:
        output_file.write(f"{token:<23}\t{lexeme}\n")

# Calculate and print total token count
total_tokens = sum(token_counts.values())
print(f"\nTotal number of Tokens: {total_tokens}")

# Print token counts
print("\nToken Counts:")
for token, count in token_counts.items():
    print(f"{token}: {count}")

# Define the grammar rules
grammar_rules = {
    "S": ["Statement"],
    "Statement": ["Assignment", "Conditional", "PrintStatement"],
    "Assignment": ["'int' identifier '=' NUMBER ';'"],
    "identifier": ["'a'", "'b'", "'c'", "'x'", "'y'", "'z'", "'r'"],
    "NUMBER": ["DIGIT", "DIGIT DIGITS"],
    "DIGIT": ["'0'", "'1'", "'2'", "'3'", "'4'", "'5'", "'6'", "'7'", "'8'", "'9'"],
    "DIGITS": ["DIGIT", "DIGIT DIGITS"],
    "Conditional": ["'if' '(' identifier '>' NUMBER ')' '{' Statement '}'"],
    "PrintStatement": ["'print' '(' Variable ')' ';'"]
}
# Create the table headers
print("\nGrammar Table:")
print("\nRule\t\t\tComponents")
# Create the table data
for rule, components in grammar_rules.items():
    print(f"{rule:<23} {', '.join(components)}")

# Define regular expressions
regex_patterns = {
    "Assignment": r"int\s+[a-zA-Z_][a-zA-Z0-9_]*\s*=\s*(\d+|\d+\s*\+\s*\d+)\s*;",
    "Conditional": r"if\s*\(\s*[a-zA-Z_][a-zA-Z0-9_]*\s*>\s*\d+\s*\)\s*\{\s*Statement\s*\}",
    "PrintStatement": r"print\s*\(\s*[a-zA-Z_][a-zA-Z0-9_]*\s*\)\s*;",
    "identifier": r"[a-zA-Z_][a-zA-Z0-9_]*",
    "NUMBER": r"\d+|\d+\s*\+\s*\d+"
}

print("\nRegular Expressions:")
for rule, pattern in regex_patterns.items():
    print(f"{rule}: {pattern}")
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
    "statement": ["assignment_stmt", "if_stmt", "loop_stmt"],
    "assignment_stmt": ["identifier", "=", "expression"],
    "if_stmt": ["if", "condition", ":", "suite"],
    "loop_stmt": ["for", "identifier", "in", "range", "(", "number", ")", ":", "suite"],
    "expression": ["identifier", "number", "expression", "+", "expression",
                   "-", "expression", "*", "expression", "/", "express"],
    "condition": ["expression", "comparison_operator", "number"],
    "comparison_operator": [">", "<", ">=", "<=", "==", "!="],
    "identifier": "[a-zA-Z_][a-zA-Z0-9_]*",
    "number": "[0-9]+"
}

# Create the table headers
print("\nGrammar Table:")
print("\nRule\t\t\tComponents")
# Create the table data
for rule, components in grammar_rules.items():
    print(f"{rule:<23} {', '.join(components)}")

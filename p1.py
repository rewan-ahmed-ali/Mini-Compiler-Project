import re
#open file
with open('text.txt', 'r') as file:
    file_contents = file.read()
split_text = re.findall(r'\b\w+\b|[^\w\s]', file_contents)
print(split_text)

# Define a function to determine the token for a lexeme
def determine_token(lexeme):
    if lexeme.isnumeric():
        return "NUMBER"
    elif lexeme in ["for", "while","if","else"]:
        return lexeme.upper()  # Return the keyword as token in uppercase
    elif lexeme.isalpha():
        return "IDENTIFIER"
    else:
        return "OPERATOR"
print("LEXEME          TOKEN")
# Print the token-lexeme pairs with lexemes in one column and tokens in the other
for lexeme in split_text:
    token = determine_token(lexeme)
    
    print(f"{lexeme:<15} {token}")

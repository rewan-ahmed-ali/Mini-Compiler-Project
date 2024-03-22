import nltk

# Define the extended context-free grammar
variable_declaration_cfg = nltk.CFG.fromstring("""
    S -> Statement
    Statement -> Assignment | Conditional | PrintStatement
    Assignment -> 'int' Variable '=' NUMBER ';'
    Variable -> 'a' | 'b' | 'c' | 'x' | 'y' | 'z' | 'r'
    NUMBER ->  DIGIT | DIGIT DIGITS
    DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    DIGITS -> DIGIT | DIGIT DIGITS
    Conditional -> 'if' '(' Variable '>' NUMBER ')' '{' Statement '}'
    PrintStatement -> 'print' '(' Variable ')' ';'
""")

# Create a parser based on the grammar
parser = nltk.ChartParser(variable_declaration_cfg)

# Read from text.txt
with open('text.txt', 'r') as file:
    lines = file.readlines()

# Parse each line and draw parse trees
for line in lines:
    # Tokenize the statement properly
    tokens = nltk.word_tokenize(line.strip())

    # Parse the statement using the provided parser
    for tree in parser.parse(tokens):
        # Define function to traverse tree and print in specified format
        def print_tree(tree, indent=0):
            if isinstance(tree, nltk.Tree):
                print(' ' * indent + tree.label())
                for subtree in tree:
                    print_tree(subtree, indent + 4)
            else:
                print(' ' * indent + str(tree))

        # Print the parse tree in the specified format
        print_tree(tree)

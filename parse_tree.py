import nltk
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        if level == 0:
            print(self.value)  # Print root node only once
        else:
            print("│    " * (level - 1) + "└───" + self.value)
        
        for child in self.children:
            child.print_tree(level + 1)


# Creating nodes
program = TreeNode("Tree Structure:\n")
read_file = TreeNode("Read text.txt")
declaration_statements = TreeNode("Declaration Statements")
conditional_statement = TreeNode("Conditional Statement (if)")

int_r = TreeNode("int r = 16;")
int_a = TreeNode("int a = 1;")
int_x = TreeNode("int x = 5;")
condition = TreeNode("Condition: x > 0")
code_block = TreeNode("Code Block")
print_statement = TreeNode("Print Statement")
expression_x = TreeNode("Expression: x")

# Building the tree structure
program.add_child(declaration_statements)
program.add_child(conditional_statement)

declaration_statements.add_child(int_r)
declaration_statements.add_child(int_a)
declaration_statements.add_child(int_x)

conditional_statement.add_child(condition)
conditional_statement.add_child(code_block)
code_block.add_child(print_statement)
print_statement.add_child(expression_x)

# Printing the tree structure
program.print_tree()

# Define the extended context-free grammar
variable_declaration_cfg = nltk.CFG.fromstring("""
    S -> Statement
    Statement -> Assignment | Conditional | PrintStatement
    Assignment -> 'int' identifier '=' NUMBER ';'
    identifier -> 'a' | 'b' | 'c' | 'x' | 'y' | 'z' | 'r'
    NUMBER ->  DIGIT | DIGIT DIGITS
    DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    DIGITS -> DIGIT | DIGIT DIGITS
    Conditional -> 'if' '(' identifier '>' NUMBER ')' '{' Statement '}'
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
        print(tree)
        # tree.pretty_print()

import nltk

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, level=0):
        if level == 0:
            print(self.value)  
        else:
            print("│    " * (level - 1) + "└───" + self.value)
        
        for child in self.children:
            child.print_tree(level + 1)


# context-free grammar
variable_declaration_cfg = nltk.CFG.fromstring("""
    S -> Statement
    Statement -> Assignment | Conditional | PrintStatement
    Assignment -> 'int' identifier '=' NUMBER ';'
    Assignment -> 'float' identifier '=' NUMBER ';'                                           
    identifier -> 'a' | 'b' | 'c' | 'x' | 'y' | 'z' | 'r'
    NUMBER ->  DIGIT | DIGIT DIGITS
    DIGIT -> '0' | '1' | '2' | '3' | '4' | '5' | '6' | '7' | '8' | '9'
    DIGITS -> DIGIT | DIGIT DIGITS
    Conditional -> 'if' '(' identifier '>' NUMBER ')' '{' Statement '}'
    PrintStatement -> 'print' '(' Variable ')' ';'
""")

# Create a parser based on the grammar
parser = nltk.ChartParser(variable_declaration_cfg)

with open('text.txt', 'r') as file:
    lines = file.readlines()


for line in lines:
    if "float" not in line:  # Skip lines containing "float"
        # Tokenize the statement properly
        tokens = nltk.word_tokenize(line.strip())
        
        # Create a root node for the parse tree
        program_tree = TreeNode("Parse Tree:")
        
        # Parse the statement using the provided parser
        for tree in parser.parse(tokens):
            # Convert the NLTK Tree to a tree structure using TreeNode class
            def convert_nltk_tree_to_tree_node(nltk_tree, parent_node):
                if isinstance(nltk_tree, nltk.Tree):
                    node = TreeNode(nltk_tree.label())
                    parent_node.add_child(node)
                    for child in nltk_tree:
                        convert_nltk_tree_to_tree_node(child, node)
                else:
                    parent_node.add_child(TreeNode(str(nltk_tree)))
            
            # Convert and add the parse tree to the program_tree
            convert_nltk_tree_to_tree_node(tree, program_tree)
            
            # Print the program_tree
            program_tree.print_tree()



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
    if "float" not in line:  # Skip lines containing "float"
        # Tokenize the statement properly
        tokens = nltk.word_tokenize(line.strip())
        # Parse the statement using the provided parser
        for tree in parser.parse(tokens):
            print(tree)
            tree.pretty_print()
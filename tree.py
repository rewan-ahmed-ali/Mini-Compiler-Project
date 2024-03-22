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
program = TreeNode("Program")
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

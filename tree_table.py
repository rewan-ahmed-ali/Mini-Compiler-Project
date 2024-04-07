class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

def build_symbol_table(file_name):
    root = TreeNode(None)  # Root node
    current_scope = root

    with open(file_name, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('if') or line.startswith('else'):
                continue  # Ignoring if-else conditions for simplicity
            if line.endswith('}') and current_scope != root:
                current_scope = current_scope.parent
                continue

            tokens = line.split()
            data_type = tokens[0]
            identifier = tokens[1]
            new_node = TreeNode((data_type, identifier))

            if line.endswith('{'):
                current_scope.children.append(new_node)
                new_node.parent = current_scope
                current_scope = new_node
            else:
                current_scope.children.append(new_node)

    return root


def print_tree(node, depth=0, is_left=False):
    if node is not None:
        if node.data:
            print("  " * depth, end='')
            print(f"|L|{node.data[1]}|......|R")
        for idx, child in enumerate(node.children):
            if is_left:
                print_tree(child, depth + 1, idx == 0)  # Draw on left
            else:
                print_tree(child, depth + 1, idx == len(node.children) - 1)  # Draw on right


file_name = "text.txt"
symbol_table_root = build_symbol_table(file_name)
print_tree(symbol_table_root)

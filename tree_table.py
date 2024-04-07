class TreeNode:
    def __init__(self, data):
        self.data = data
        self.link = None  # Link field for the linked list
        self.parent = None

def build_symbol_table(file_name):
    root = TreeNode(None)  # Root node
    current_scope = root
    first_node = None

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
                if not first_node:
                    first_node = new_node
                else:
                    current_scope.link = new_node  # Linking the new node to the previous one
                current_scope = new_node
            else:
                if not first_node:
                    first_node = new_node
                else:
                    current_scope.link = new_node
                current_scope = new_node

    return first_node  # Return the pointer to the first record


def print_linked_list(first_node):
    current_node = first_node
    while current_node:
        print(f"|L|{current_node.data[1]}|......|R")
        current_node = current_node.link


file_name = "text.txt"
first_record = build_symbol_table(file_name)
print_linked_list(first_record)

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    else:
        if value < root.value:
            root.left = insert(root.left, value)
        else:
            root.right = insert(root.right, value)
    return root

def print_tree(root, level=0, direction='Root', indent=0):
    if root is not None:
        if level == 0:
            print(' ' * indent + direction + ':', root.value)
        else:
            print(' ' * indent + direction + ':', root.value)
        print_tree(root.left, level + 1, 'Left', indent - 20)
        print_tree(root.right, level + 1, 'Right', indent + 10)

def main():
    variables = []
    with open('text.txt', 'r') as file:
        for line in file:
            if line.strip().startswith(('int', 'float')):
                variable = line.split()[1].strip()
                variables.append(variable)
    
    # Construct the binary search tree
    root = None
    for item in variables:
        root = insert(root, item)
    print_tree(root, indent=20)

if __name__ == "__main__":
    main()

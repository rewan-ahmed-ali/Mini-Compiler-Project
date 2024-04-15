class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return TreeNode(value)
    else:
        if value < root.data:
            if root.left is None:
                root.left = TreeNode(value)
            else:
                insert(root.left, value)
        else:
            if root.right is None:
                root.right = TreeNode(value)
            else:
                insert(root.right, value)
    return root

def print_tree(root, level=0, direction='Root', indent=0):
    if root is not None:
        if level == 0:
            print(' ' * indent + direction + ':', "|L|" + root.data + "|....|R|")
        else:
            print(' ' * indent + direction + ':', "|L|" + root.data + "|....|R|")
        print_tree(root.left, level + 1, 'Left', indent - 30)
        print_tree(root.right, level + 1, 'Right', indent + 20)

def main():
    variables = []
    with open('text.txt', 'r') as file:
        for line in file:
            if line.strip().startswith(('int', 'float')):
                variable = line.split()[1].strip()
                variables.append(variable)
    
    # Binary Tree Symbol Table
    root = None
    for item in variables:
        root = insert(root, item)
    print("\nTree Structure Symbol Table:\n")
    print_tree(root, indent=20)

if __name__ == "__main__":
    main()

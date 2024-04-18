def calculate_first_sets(grammar):
    first_sets = {}
    
    # Initialize first sets for terminals
    for terminal in terminals(grammar):
        first_sets[terminal] = {terminal}
    
    # Initialize first sets for non-terminals
    for non_terminal in non_terminals(grammar):
        first_sets[non_terminal] = set()
    
    # Iterate until no more changes occur in first sets
    while True:
        changes = False
        for non_terminal, production in grammar:
            first_symbol = production[0]
            if first_symbol in first_sets:
                if add_first_set(first_sets[non_terminal], first_sets[first_symbol]):
                    changes = True
                # If first symbol is a non-terminal, check if it derives epsilon
                if 'epsilon' in first_sets[first_symbol]:
                    index = 1
                    # Continue adding next symbols until epsilon is not derived
                    while index < len(production) and 'epsilon' in first_sets[first_symbol]:
                        if production[index] in first_sets:
                            if add_first_set(first_sets[non_terminal], first_sets[production[index]] - {'epsilon'}):
                                changes = True
                        index += 1
        if not changes:
            break
    
    return first_sets


def add_first_set(target_set, new_set):
    old_size = len(target_set)
    target_set |= new_set
    return len(target_set) != old_size


def non_terminals(grammar):
    return set(non_terminal for non_terminal, _ in grammar)


def terminals(grammar):
    terminals_set = set()
    for _, production in grammar:
        for symbol in production:
            if symbol not in non_terminals(grammar):
                terminals_set.add(symbol)
    return terminals_set


def main():
    grammar = [
        ('E', 'TA'),
        ('A', '+TA'),
        ('A', 'epsilon'),
        ('T', 'FB'),
        ('B', '*FB'),
        ('B', 'epsilon'),
        ('F', '(E)'),
        ('F', 'd'),
    ]

    first_sets = calculate_first_sets(grammar)

    # Print the calculated FIRST sets
    for non_terminal, first_set in first_sets.items():
        print(f'First({non_terminal})={first_set}')


if __name__ == '__main__':
    main()

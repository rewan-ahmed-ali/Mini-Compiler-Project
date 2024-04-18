def calculate_first_sets(grammar):
    first_sets = {}
    for terminal in terminals(grammar):
        first_sets[terminal] = {terminal}
    for non_terminal in non_terminals(grammar):
        first_sets[non_terminal] = set()
    while True:
        changes = False
        for non_terminal, production in grammar:
            first_symbol = production[0]
            if first_symbol in first_sets:
                if add_first_set(first_sets[non_terminal], first_sets[first_symbol]):
                    changes = True
                if 'epsilon' in first_sets[first_symbol]:
                    index = 1
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
    for non_terminal, first_set in first_sets.items():
        # Replace "e" with "epsilon"
        first_set_str = '{' + ', '.join(symbol if symbol != 'e' else 'epsilon' for symbol in first_set) + '}'
        print(f'First({non_terminal})={first_set_str}')

if __name__ == '__main__':

    main()

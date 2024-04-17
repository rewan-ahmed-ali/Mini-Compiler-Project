def calculate_first(grammar):
    first = {}
    for non_terminal in grammar:
        first[non_terminal] = set()

    def calculate_first_helper(symbol):
        if symbol in first:
            return first[symbol]

        for production in grammar[symbol]:
            for symbol in production:
                first_set = calculate_first_helper(symbol)
                first[symbol].update(first_set)
                if 'e' not in first_set:
                    break
            else:
                first[symbol].add('e')

        return first[symbol]

    for non_terminal in grammar:
        calculate_first_helper(non_terminal)

    return first


# Define the grammar
grammar = {
    'E': [['T', 'E\'']],
    'E\'': [['+', 'T', 'E\''], ['']],
    'T': [['F', 'T\'']],
    'T\'': [['*', 'F', 'T\''], ['']],
    'F': [['(', 'E', ')'], ['id']]
}

# Calculate the First sets
first_sets = calculate_first(grammar)

# Print the First sets
for non_terminal, terminals in first_sets.items():
    print(f"First({non_terminal}) = {terminals}")
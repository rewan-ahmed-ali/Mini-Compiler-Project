
def first(grammar, symbol):
    first_set = set()
    symbol_set = {
        prod[1] for prod in grammar if prod[0] == symbol
    }
    for element in symbol_set:
        if element == 'epsilon':
            first_set.add(element)
        elif not element[0].isupper():
            first_set.add(element[0])
        else:
            first_set |= Production_rule_3(grammar, element)

    return first_set

def Production_rule_3(grammar, element):
    first_set = set()
    i = 0
    while i < len(element):
        first_i = first(grammar, element[i])
        first_set |= first_i.difference({'epsilon'})
        if 'epsilon' not in first_i:
            break
        i += 1
    return first_set

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
non_terminals_set = set(left_side for left_side, _ in grammar)
terminals_set = set()
for nt in non_terminals_set:
    terminals_set |= first(grammar, nt).difference({'epsilon'})
non_terminals = list(non_terminals_set)
terminals = list(terminals_set)

print("First Sets:")
for nt in non_terminals:
    print(f'First({nt}) = {first(grammar, nt)}')

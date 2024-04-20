from prettytable import PrettyTable

# تعريف دالة First
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

# تعريف دالة Production_rule_3
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

# تعريف دالة Follow
def follow(grammar, start_symbol, symbol):
    follow_set = set()

    if symbol == start_symbol:
        follow_set.add('$')
    for production in grammar:
        if symbol in production[1]:
            prodc = production[1]
            if symbol == prodc[-1]:
                follow_set |= follow(grammar, start_symbol, production[0])
                return follow_set

    for element in (prod[1] for prod in grammar if symbol in prod[1]):
        for symb in element[element.index(symbol)+1:]:
            if not symb.isupper():
                follow_set.add(symb)
                break
            else:
                first_symb = first(grammar, symb)
                if "epsilon" in first_symb:
                    follow_set |= first_symb.difference({'epsilon'})
                    follow_set |= follow(grammar, start_symbol, symb)
                else:
                    follow_set |= first_symb
    return follow_set

# تحديد القواعد النحوية الجديدة
grammar = [
    ('S', 'ID = NUM;'),
    ('S', 'ID = FLOAT_NUM;'),
    ('ID', 'ID1'),
    ('ID1', 'int'),
    ('ID1', 'float'),
    ('NUM', '1'),
    ('FLOAT_NUM', '1.2'),
    ('S', 'if ( EXPR ) { STMT }'),
    ('EXPR', 'NUM'),
    ('EXPR', 'FLOAT_NUM'),
    ('STMT', 'print ( EXPR )')
]

# تحديد الرموز non_terminals  terminals
non_terminals_set = set(left_side for left_side, _ in grammar)
terminals_set = set()
for nt in non_terminals_set:
    terminals_set |= {c for c in nt if c.islower()}
    terminals_set |= {c for c in nt if c.isnumeric()}
    terminals_set |= {'=', '(', ')', ';', 'if', 'print'}

non_terminals = sorted(list(non_terminals_set))
terminals = sorted(list(terminals_set))

# تحديد القوائم First و Follow
first_sets = {}
follow_sets = {}

for nt in non_terminals:
    first_sets[nt] = first(grammar, nt)
    follow_sets[nt] = follow(grammar, "S", nt)


grammar_table = PrettyTable()
grammar_table.field_names = ['Non-terminal', 'Production']
for rule in grammar:
    grammar_table.add_row([rule[0], rule[1]])


first_table = PrettyTable()
first_table.field_names = ['Non-terminal', 'First Set']
for nt in non_terminals:
    first_table.add_row([nt, first_sets[nt]])


follow_table = PrettyTable()
follow_table.field_names = ['Non-terminal', 'Follow Set']
for nt in non_terminals:
    follow_table.add_row([nt, follow_sets[nt]])


parse_table = PrettyTable()
parse_table.field_names = ['NT / T'] + terminals
for nt in non_terminals:
    productions = [prod[1] for prod in grammar if prod[0] == nt and prod[1] != 'epsilon']
    row_values = []
    first_nt = first_sets[nt]
    follow_nt = follow_sets[nt]
    for t in terminals:
        if t in first_nt:
            row_values.append(f'{nt} => {productions}')
        elif 'epsilon' in first_nt and t in follow_nt:
            row_values.append(f'{nt} => epsilon')
        else:
            row_values.append('')
    parse_table.add_row([nt] + row_values)


print("Grammar Rules:")
print(grammar_table)
print("\nFirst Sets:")
print(first_table)
print("\nFollow Sets:")
print(follow_table)
print("\nParse Table:")
print(parse_table)
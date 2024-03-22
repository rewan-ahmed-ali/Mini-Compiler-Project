import re

# Function to extract variables and their attributes from a line
def extract_variables(line):
    variables = re.findall(r'\b(?:int|float|char)\s+([a-zA-Z_]\w*)\s*=?\s*([^;]*)', line)
    return variables

# Function to construct the symbol table for a line
def construct_symbol_table(line, line_number, counter):
    symbol_table = []
    variables = extract_variables(line)
    for var_name, var_declaration in variables:
        data_type = var_declaration.split('=')[0].strip()
        # Assuming no array declarations in this example
        dimension = 0
        line_declaration = line_number
        line_reference = []
        symbol_table.append({
            'counter': counter,
            'variable_name': var_name,
            'code_address': None,  # Placeholder for code address
            'datatype': data_type,
            'dimension': dimension,
            'line_declaration': line_declaration,
            'line_reference': line_reference
        })
    return symbol_table, counter + 1

# Function to read text file and construct symbol table for each line
def process_text_file(filename):
    symbol_tables = []
    counter = 0
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i, line in enumerate(lines):
            line_number = i + 1
            symbol_table, counter = construct_symbol_table(line.strip(), line_number, counter)
            symbol_tables.extend(symbol_table)
    return symbol_tables

# Main function
def main():
    filename = 'text.txt'
    symbol_tables = process_text_file(filename)
    # Print symbol tables for each line
    for i, table in enumerate(symbol_tables):
        print(f"Line {i+1} Symbol Table:")
        for key, value in table.items():
            print(f"{key}: {value}")
        print()

if __name__ == "__main__":
    main()

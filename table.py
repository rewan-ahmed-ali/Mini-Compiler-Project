import re

def generate_symbol_table(code):
    """
    Generates a symbol table from the given code.

    Args:
        code (str): The code to analyze.

    Returns:
        list: A list of dictionaries representing the symbol table entries.
    """

    symbol_table = []
    line_number = 1
    current_address = 0  # Starting memory address

    for line in code.splitlines():
        # Extract variable declarations
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_name = match.group("variable_name")

            # Add entry to symbol table
            symbol_table.append({
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": [line_number]
            })

            # Increment memory address
            current_address += 2  # Assuming each variable occupies 4 bytes

        # Track variable references
        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    entry["Reference Line"] += [line_number]
                    break

        line_number += 1

    return symbol_table

# Read code from file
with open('text.txt', 'r') as file:
    code = file.read()

# Generate symbol table
symbol_table = generate_symbol_table(code)

# Print the symbol table
print("Symbol Table:")
for entry in symbol_table:
    print(entry)

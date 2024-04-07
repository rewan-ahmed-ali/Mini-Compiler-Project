import re

def generate_symbol_table(code):
    symbol_table = []
    line_number = 1
    current_address = 0  # Starting memory address
    counter = 0

    for line in code.splitlines():
        # Extract variable declarations
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_name = match.group("variable_name")

            # Add entry to symbol table
            if not symbol_table:  # First entry
                counter = 0
            else:
                counter += 1

            symbol_table.append({
                "Counter": counter,
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set([line_number]),  # Change list to set
                
            })

            # Increment memory address
            current_address += 2  # Assuming each variable occupies 4 bytes

        # Track variable references
        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    entry["Reference Line"].add(line_number)  # Change list to set
                    break

        line_number += 1

    return symbol_table

# Read code from file
with open('text.txt', 'r') as file:
    code = file.read()

# Generate symbol table
symbol_table = generate_symbol_table(code)

# Print the symbol table with spaces between entries
print("Unorderd Symbol Table:\n")
for entry in symbol_table:
    print(entry)
    print()  # Add a newline after each entry

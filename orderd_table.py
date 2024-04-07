import re

def generate_symbol_table(code):
    symbol_table = []
    line_number = 1
    current_address = 0  
    counter = 0

    for line in code.splitlines():
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_name = match.group("variable_name")

            # Add entry to symbol table
            symbol_table.append({
                "Counter": counter,  # Counter at the beginning
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set([line_number])  # Change to set to avoid duplicates
            })
            current_address += 2  
            counter += 1  # Increment counter

        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    entry["Reference Line"].add(line_number)  # Change to set to avoid duplicates
                    break

        line_number += 1

    # Sort symbol table entries by variable name
    symbol_table.sort(key=lambda x: x["Variable Name"])

    # Update counter after sorting
    for i, entry in enumerate(symbol_table):
        entry["Counter"] = i

    # Update address based on sorted order
    for i, entry in enumerate(symbol_table):
        entry["Address"] = i * 2
    
    return symbol_table

with open('text.txt', 'r') as file:
    code = file.read()

symbol_table = generate_symbol_table(code)

print("Symbol Table:")
for entry in symbol_table:
    print(entry)
    print()

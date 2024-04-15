import re

def generate_symbol_table(code):
    symbol_table = []
    line_number = 1
    current_address = 0  
    counter = 0

    for line in code.splitlines():
        # Extract variable declarations
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_name = match.group("variable_name")

            # Add entry to symbol table
            symbol_table.append({
                "Counter": counter,  
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set(),  
            })
            current_address += 2  

        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    # Only add line number if it's not the declaration line
                    if line_number != entry["Line Declaration"]:
                        entry["Reference Line"].add(line_number)
                    break

        line_number += 1

    # Sort symbol table alphabetically by variable name
    symbol_table.sort(key=lambda x: x["Variable Name"])

    # Reset the Counter values
    for entry in symbol_table:
        entry["Counter"] = counter
        counter += 1
    
    # Update addresses based on the new order
    for entry in symbol_table:
        entry["Address"] = symbol_table.index(entry) * 2

    return symbol_table


with open('text.txt', 'r') as file:
    code = file.read()

symbol_table = generate_symbol_table(code)


print("Ordered Symbol Table:\n")
for entry in symbol_table:
    # Print with empty {} instead of set()
    print(str(entry).replace("set()", "{}")) 
    print()  

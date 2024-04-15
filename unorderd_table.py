import re
#unorderd Symbol Table
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

            # symbol table
            symbol_table.append({
                "Counter": counter,
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set(),  # Initialize as an empty set
            })
            counter+=1
            current_address += 2  


        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    # Only add line number if it's not the declaration line
                    if line_number != entry["Line Declaration"]:
                        entry["Reference Line"].add(line_number)
                    break

        line_number += 1

    return symbol_table

# Read code from file
with open('text.txt', 'r') as file:
    code = file.read()

symbol_table = generate_symbol_table(code)

# Print the symbol table with spaces between entries
print("\nUnordered Symbol Table:\n")
print(f"{'Counter':<8}{'Variable Name':<15}{'Address':<10}{'Data Type':<15}{'No. of Dimensions':<20}{'Line Declaration':<20}{'Reference Line'}")
for entry in symbol_table:
    # Print empty {} instead of set()
    print(f"{entry['Counter']:<8}{entry['Variable Name']:<15}{entry['Address']:<10}{entry['Data Type']:<15}{entry['No. of Dimensions']:<20}{entry['Line Declaration']:<20}{str(entry['Reference Line']).replace('set()', '{}')}")
print()  # Add a newline after the table

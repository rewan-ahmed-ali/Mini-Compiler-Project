import re

def generate_symbol_table(code):
    symbol_table = []
    line_number = 1
    current_address = 0  

    for line in code.splitlines():
        match = re.match(r"^\s*(?P<data_type>\w+)\s+(?P<variable_name>\w+)\s*=\s*(?P<value>.+);$", line)
        if match:
            data_type = match.group("data_type")
            variable_name = match.group("variable_name")
            symbol_table.append({
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set([line_number])  # Change to set to avoid duplicates
            })
            current_address += 2  

        for variable in re.findall(r"\b\w+\b", line):
            for entry in symbol_table:
                if entry["Variable Name"] == variable:
                    entry["Reference Line"].add(line_number)  # Change to set to avoid duplicates
                    break

        line_number += 1

    symbol_table.sort(key=lambda x: x["Variable Name"])
    
    return symbol_table

with open('text.txt', 'r') as file:
    code = file.read()

symbol_table = generate_symbol_table(code)

print("Symbol Table:")
for entry in symbol_table:
    print(entry)

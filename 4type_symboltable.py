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

#orderd Symbol Table

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

            #  symbol table
            symbol_table.append({
                "Counter": counter, 
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set(),  # empty set
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
print(f"{'Counter':<8}{'Variable Name':<15}{'Address':<10}{'Data Type':<15}{'No. of Dimensions':<20}{'Line Declaration':<20}{'Reference Line'}")
for entry in symbol_table:
    print(f"{entry['Counter']:<8}{entry['Variable Name']:<15}{entry['Address']:<10}{entry['Data Type']:<15}{entry['No. of Dimensions']:<20}{entry['Line Declaration']:<20}{str(entry['Reference Line']).replace('set()', '{}')}")
print()  

#Hash Symbol Table

def calculate_hash(variable_name, hash_max):
    variable_length = len(variable_name)  # Calculate the length of the variable name
    ascii_sum = sum(ord(char) for char in variable_name)  # Calculate the sum of ASCII values
    hash_value = (variable_length + ascii_sum) % hash_max  # Calculate the hash value
    return hash_value  


file_path = "text.txt"  
symbol_table = {}  
hash_max = 3  
with open(file_path, 'r') as file:
    for line in file:
        # Remove  whitespace
        line = line.strip()
        # Ignore empty lines
        if not line:
            continue
        
        # Extract variable name from the line
        match = re.match(r"^\s*\w+\s+(\w+)\s*=", line)
        if match:
            variable_name = match.group(1)
        else:
            continue
        # Calculate the hash and store it in the symbol table
        hash_value = calculate_hash(variable_name, hash_max)
        symbol_table[variable_name] = hash_value

print("Hash Symbol Table:\n")
for variable_name, hash_value in symbol_table.items():
    print(f"hash({variable_name}) = ({len(variable_name)} + {'+'.join(str(ord(char)) for char in variable_name)}) % {hash_max} = {hash_value}")
print(f"\n{'Variable Name':<15}{'Hash Value'}")
for variable_name, hash_value in symbol_table.items():
    print(f"{variable_name:<15}{hash_value}")

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
            symbol_table.append({
                "Counter": counter,
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set(),  # Initialize as an empty set
            })

            # Increment memory address
            current_address += 2  # Assuming each variable occupies 4 bytes

        # Track variable references (modified)
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

# Generate symbol table
symbol_table = generate_symbol_table(code)

# Print the symbol table with spaces between entries
print("Unordered Symbol Table:\n")
for entry in symbol_table:
    # Print with empty {} instead of set()
    print(str(entry).replace("set()", "{}")) 
    print()  # Add a newline after each entry

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
            symbol_table.append({
                "Counter": 0,  # Start with Counter as 0
                "Variable Name": variable_name,
                "Address": current_address,
                "Data Type": data_type,
                "No. of Dimensions": 0,
                "Line Declaration": line_number,
                "Reference Line": set(),  # Initialize as an empty set
            })

            # Increment memory address
            current_address += 2  # Assuming each variable occupies 4 bytes

        # Track variable references (modified)
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

# Read code from file
with open('text.txt', 'r') as file:
    code = file.read()

# Generate symbol table
symbol_table = generate_symbol_table(code)

# Print the symbol table with spaces between entries
print("Ordered Symbol Table:\n")
for entry in symbol_table:
    # Print with empty {} instead of set()
    print(str(entry).replace("set()", "{}")) 
    print()  # Add a newline after each entry


import re

def calculate_hash(variable_name, hash_max):
    variable_length = len(variable_name)  # Calculate the length of the variable name
    ascii_sum = sum(ord(char) for char in variable_name)  # Calculate the sum of ASCII values
    hash_value = (variable_length + ascii_sum) % hash_max  # Calculate the hash value
    return hash_value  # Return the calculated hash value

# Read from the text file
file_path = "text.txt"  # Update with your file path
symbol_table = {}  # Initialize the symbol table
hash_max = 3  # Example value for hash max

# Open the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Remove leading/trailing whitespace
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

print("\nHash Symbol Table:")
for variable_name, hash_value in symbol_table.items():
    print(f"hash({variable_name}) = ({len(variable_name)} + {'+'.join(str(ord(char)) for char in variable_name)}) % {hash_max} = {hash_value}")

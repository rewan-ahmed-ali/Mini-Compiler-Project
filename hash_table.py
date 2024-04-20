import re
def calculate_hash(variable_name, hash_max):
    variable_length = len(variable_name)  # Calculate the length of the variable name
    ascii_sum = sum(ord(char) for char in variable_name)  # Calculate the sum of ASCII values
    hash_value = (variable_length + ascii_sum) % hash_max  # Calculate the hash value
    return hash_value  


file_path = "text.txt"  
symbol_table = {}  
hash_max = 4  
with open(file_path, 'r') as file:
    for line in file:
        # Remove whitespace
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

print("Hash Symbol Table:")
for variable_name, hash_value in symbol_table.items():
    print(f"hash({variable_name}) = ({len(variable_name)} + {'+'.join(str(ord(char)) for char in variable_name)}) % {hash_max} = {hash_value}")

print(f"\n{'Variable Name':<15}{'Hash Value'}")
for variable_name, hash_value in symbol_table.items():
    print(f"{variable_name:<15}{hash_value}")
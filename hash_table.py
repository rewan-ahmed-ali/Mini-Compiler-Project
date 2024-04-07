# Define the hash function based on the provided formula
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
        
        # Check if the line starts with "int"
        if line.startswith("int"):
            # Split the line by "=" to extract variable name and value
            parts = line.split("=")
            # Check if there are at least two parts (variable name and value)
            if len(parts) < 2:
                continue  # Skip lines without assignment
            variable_name = parts[0].split()[1].strip()  # Extract variable name after "int"
        else:
            # Split the line by "=" to extract variable name and value
            parts = line.split("=")
            # Check if there are at least two parts (variable name and value)
            if len(parts) < 2:
                continue  # Skip lines without assignment
            variable_name = parts[0].strip()
        
        variable_value = parts[1].strip()
        # Calculate the hash and store it in the symbol table
        hash_value = calculate_hash(variable_name, hash_max)
        symbol_table[variable_name] = hash_value


print("Hash Symbol Table:")
for variable_name, hash_value in symbol_table.items():
    print(f"hash({variable_name}) = ({len(variable_name)} + {'+'.join(str(ord(char)) for char in variable_name)}) % {hash_max} = {hash_value}")

# Define the hash function based on the provided formula
def calculate_hash(variable_name, hash_max):
    ascii_sum = sum(ord(char) for char in variable_name)  # Calculate the sum of ASCII values
    variable_length = len(variable_name)  # Calculate the length of the variable name
    hash_value = (variable_length + ascii_sum) % hash_max  # Calculate the hash value
    return hash_value  # Return the calculated hash value

# Read from the text file
file_path = "text.txt"  # Update with your file path
symbol_table = {}  # Initialize the symbol table
hash_max = 3  # Example value for hash max

# Open the file and process each line
with open(file_path, 'r') as file:
    for line in file:
        # Remove leading/trailing whitespace and ignore empty lines
        line = line.strip()
        if not line:
            continue
        
        # Check for the variable assignment pattern
        if '=' in line:
            parts = line.split('=')
            variable_name = parts[0].strip()
            variable_value = parts[1].strip()
            # Calculate the hash and store it in the symbol table
            hash_value = calculate_hash(variable_name, hash_max)
            symbol_table[variable_name] = hash_value

# Print the hash values for each variable
print("Hash values:")
for variable_name, hash_value in symbol_table.items():
    print(f"hash({variable_name})=({len(variable_name)}+{sum(ord(char) for char in variable_name)})%{hash_max}={hash_value}")

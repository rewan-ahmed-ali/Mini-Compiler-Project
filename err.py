import re

def parse_text_file(file_path):
    grammar_errors = []
    variables = {}  # Dictionary to store variable assignments

    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line_num, line in enumerate(lines, start=1):
            line = line.strip()
            if not line:
                continue

            # Check for variable assignment with arithmetic expression
            match = re.match(r'^(\w+)\s*=\s*(.*?)$', line)
            if match:
                variable, expression = match.groups()
                if not variable.isidentifier():
                    grammar_errors.append(f"Error in line {line_num}: Invalid identifier  '{variable}'.")
                elif variable[0].isupper():
                    grammar_errors.append(f"Error in line {line_num}: Uppercase variable names are not supported.")
                else:
                    variables[variable] = expression
                continue

            # Check for constraints x + y = 5 or x * y = 10
            match = re.match(r'^(\w+)\s*([+*])\s*(\w+)\s*=\s*(\d+)$', line)
            if match:
                var1, operator, var2, result = match.groups()
                if operator == '+':
                    if var1 in variables and var2 in variables:
                        if int(variables[var1]) + int(variables[var2]) != int(result):
                            grammar_errors.append(f"Error in line {line_num}: Constraint '{var1} + {var2} = {result}' not satisfied.")
                    else:
                        grammar_errors.append(f"Error in line {line_num}: identifier not exist.")
                elif operator == '*':
                    if var1 in variables and var2 in variables:
                        if int(variables[var1]) * int(variables[var2]) != int(result):
                            grammar_errors.append(f"Error in line {line_num}: Constraint '{var1} * {var2} = {result}' not satisfied.")
                    else:
                        grammar_errors.append(f"Error in line {line_num}: identifier not exist")
                else:
                    grammar_errors.append(f"Error in line {line_num}: Invalid operator '{operator}'. Only '+' and '*' are supported.")

    return grammar_errors

def handle_errors(errors):
    if errors:
        for error in errors:
            print(error)
    else:
        print("No grammar errors found.")

def main():
    # Path to your text file
    file_path = "text.txt"

    # Parse the text file and check for grammar errors
    errors = parse_text_file(file_path)

    # Handle errors
    handle_errors(errors)

if __name__ == "__main__":
    main()
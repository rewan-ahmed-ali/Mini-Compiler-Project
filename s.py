import re

def symbol_table(source_code_path):
    # open the file
    file_ = open(source_code_path, 'r')

    # initialize the counter
    counter = 1
    
    # list of lines
    list_ = file_.readlines()
    
    # types
    types = ['int']
    
    # line references
    line_ref = []
    
    # code address intialization
    code_address = 0
    
    # initialize list_symbol
    list_symbol = []
    
    # get line reference
    for line_ in list_:
        lexers = line_.split(' ')
        for i in lexers:
            is_ident = re.match(r'\~[a-z0-9]+', i)
            if lexers[0] in types:
                continue
            else:
                if is_ident:
                    line_ref.append(list_.index(line_)+1)
    
    # get symbol table
    for line in list_:
        
        # split line into tokens
        tokens = line.split(' ')
        
        # get the token type
        token_type = tokens[0]
        # continue if tokens[0] not a datatype
        if tokens[0] not in types:
            continue
            
        # if the token type is 'int' or 'string', add it to the symbol table
        if tokens[0] == 'int':
            try:
                symbol_name = tokens[1]
            except:
                symbol_name = None
            if symbol_name == None:
                continue
                
            line_dec = list_.index(line)
            symbol_table= {
                'counter': counter,
                'variable_name': symbol_name,
                'code_address': code_address,
                'datatype': token_type,
                'dimension': 0,
                'line_declaration': line_dec+1,
                'line_reference': line_ref
            }
            counter += 1
            list_symbol.append(symbol_table)
    
    return list_symbol

source_code_path = "text.txt"
symbol_data = symbol_table(source_code_path=source_code_path)
print(symbol_data)

def first(symbol, grammar):
  """
  Calculates the First set for a given symbol in the grammar.

  Args:
      symbol: The grammar symbol for which to calculate the First set.
      grammar: A dictionary representing the grammar, where keys are non-terminals 
               and values are lists of productions.

  Returns:
      A set containing the First set for the symbol.
  """

  first_set = set()
  if symbol.islower() or symbol == "''":  # Terminal or epsilon
    first_set.add(symbol)
  else:
    for production in grammar[symbol]:
      first_symbol = production[0]
      if first_symbol == "''": 
        if len(production) > 1:
          first_set.update(first(production[1], grammar))
        else:
          first_set.add("''") 
      else:
        if first_symbol in grammar:  # Check if it's a non-terminal
          first_set.update(first(first_symbol, grammar))
        else:
          first_set.add(first_symbol) # Add the terminal directly
  return first_set

# Define your grammar
grammar = {
  "E": ["TE'"],
  "E'": ["+TE'", "''"],
  "T": ["FT'"],
  "T'": ["*FT'", "''"],
  "F": ["(E)", "id"]
}

# Calculate First sets
print("First(E) =", first("E", grammar))
print("First(E') =", first("E'", grammar))
print("First(T) =", first("T", grammar))
print("First(T') =", first("T'", grammar))
print("First(F) =", first("F", grammar))
def float_part(string, value) -> str:
    index = string.index(value)
    start = index + 1
    end = -1
    string_float_part = string[start:end]
    return string_float_part

def is_dot(char) -> bool:
  return True if char == '.' else False

def is_parentheses(char) -> bool:
  return True if char == '(' or char == ')' else False

def is_plus(char) -> bool:
  return True if char == '+' else False

def is_multiply(char) -> bool:
  char.lower()
  return True if char == 'x' else False




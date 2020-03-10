from helper import float_part, is_dot, is_parentheses, is_plus, is_multiply

def is_number(string):
  size = len(string)
  for c in range(size):
    value = string[c]
    if not value.isdigit():
      return False
  return True

def is_float(string):
  for c in range(len(string)):
    value = string[c]
    if not value.isdigit():
      if is_dot(value):
        string_float_part = float_part(string, value)
        if is_number(string_float_part):
          return True
      else:
        return False
  return False
        
entry = "2 + 40 x (3.1+444)"
print(f'The entry is: {entry}')
list_entry = entry.split()
print(f'Split: {list_entry}')

for i in range(len(list_entry)):
  value = list_entry[i] 
  if is_number(value):
    token = 'number'
  elif is_float(value):
    token = 'float'
  elif is_parentheses(value):
    token = '\'(\' or \')\''
  elif is_plus(value):
    token = '+'
  elif is_multiply(value):
    token = 'x'
  else:
    token = 'token unidentified'
  
  print(f'{value} => {token}')
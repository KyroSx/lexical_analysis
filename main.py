def is_dot(char):
  return True if char == '.' else False

def is_number(string):
  for c in range(len(string)):
    value = string[c]
    if not value.isdigit():
      return False
  return True

def is_float(string):
  for c in range(len(string)):
    value = string[c]
    if value.isdigit():
      continue
    else:
      if is_dot(value):
        if is_number(string[string.index(value) + 1:-1]):
          return True
      else:
        return False
  return False
        
entry = "2 + 3.4 x 3.1 "
list_entry = entry.split()
print(list_entry)

for i in range(len(list_entry)):
  value = list_entry[i] 
  result = is_float(value)
  print(f'{value} -> {result}')
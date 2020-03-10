'''
    palavras resenvadas, ids, simbolos, int, strings
'''
def is_reserved_word(string):
    if string == 'function':
        return True
    elif string == 'return':
        return True 
    elif string == 'const':
        return True
    return False

def is_symbol(string):
    if string == '{' or string == '}':
        return True
    elif string == '(' or string == ')':
        return True
    elif string == '+' or string == '-':
        return True
    elif string == '=' or string == ',':
        return True
    return False

def is_identifier(string):
    value = string[0]
    if value.isdigit():
        return False
    else:
        size = len(string)
        for c in range(size):
            value = string[c]
            if not value.isalnum():
                return False
    return True
    
def is_number(string):
  size = len(string)
  for c in range(size):
    value = string[c]
    if not value.isdigit():
      return False
  return True

def space(string, symbol):
    new_symbol = f' {symbol} ' 
    new_string = string.replace(symbol, new_symbol) 

def space_elements(string):
    new_value = string.replace('(', ' ( ')
    new_value = new_value.replace(')', ' ) ')
    new_value = new_value.replace(',', ' , ')
    return new_value

def format_content(string):
    size = len(string)
    for c in range(size):
        value = space_elements(string)
        return value
    pass

def get_content_file(file_name) -> list:
    file_name = f'{file_name}.txt'
    file_mode = 'r'
    file = open(file_name, file_mode)
    if file.mode == file_mode:
        content = file.read().split()
    return content

content = get_content_file('entry')
print(f'cont = {content}')
for i in range(len(content)):
    value = content[i]
    content[i] = format_content(value)

separator = ' '
content = separator.join(content).split()

for item in content:
    token = 'unidentified'
    if is_reserved_word(item):
        token = 'reserved word'
    elif is_number(item):
        token = 'number'
    elif is_identifier(item):
        token = 'indentifier'
    elif is_symbol(item):
        token = 'symbol'
    print(f'{item} => {token}')

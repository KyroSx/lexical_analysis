'''
    palavras resenvadas, ids, simbolos, int, strings
'''
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
for i in range(len(content)):
    content[i] = format_content(content[i])

print(' '.join(content).split())


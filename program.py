"""
program: BEGIN compound END DOT
compound: INTEGER
"""
LETTERS = 'abcdefghijklmnopqurstuvwtxyz' + 'ABCDEFGHIJKLMNOPQURSTUVWTXYZ'
DIGITS = '0123456789'
WHITESPACE = ' \n\t'


BEGIN = 'BEGIN'
END = 'END'
DOT_SYMBOL = '.'
DOT = 'DOT'
EOF = 'EOF'

INTEGER = 'INTEGER'


EOF_TOKEN = (EOF, EOF)
BEGIN_TOKEN = (BEGIN, BEGIN)
END_TOKEN = (END, END)
DOT_TOKEN = (DOT, DOT)


is_idx_eof = lambda x, y: y == len(x)


class ProgramNode:
    def __init__(self, node):
        self.node = node

class CompundNode:
    def __init__(self, node):
        self.intnode = node

class IntegerNode:
    def __init__(self, value):
        self.value = value



def find_identifier(src, idx):
    char = src[idx]
    result = char
    while True:
        idx += 1
        if is_idx_eof(src, idx):
            break
        char = src[idx]
        if char not in LETTERS:
            break
        result += char
    return result, idx


def find_integer(src, idx):
    result = src[idx]
    while True:
        idx += 1
        if is_idx_eof(src, idx):
            break
        if src[idx] not in DIGITS:
            break
        result += src[idx]

    number = int(result)
    return number, idx


def find_token(src, idx):
    if is_idx_eof(src, idx):
        idx += 1
        return EOF_TOKEN, idx

    char = src[idx]

    while char in WHITESPACE:
        idx += 1
        if is_idx_eof(src, idx):
            return EOF_TOKEN, idx
        char = src[idx]

    if char in LETTERS:
        identifier, idx = find_identifier(src, idx)
        if identifier == BEGIN:
            token = BEGIN_TOKEN
        elif identifier == END:
            token = END_TOKEN

    elif char == DOT_SYMBOL:
        token = DOT_TOKEN
        idx += len(DOT_SYMBOL)

    elif char in DIGITS:
        number, idx = find_integer(src, idx)
        token = (INTEGER, number)

    else:
        raise Exception('CAN`T FIND TOKEN')

    return token, idx



def compound(src, idx):
    token, idx = find_token(src, idx)
    assert token[0] == INTEGER
    node = IntegerNode(token[1])
    compnode = CompundNode(node)
    return compnode, idx



def program(src, idx):
    begin, idx = find_token(src, idx)
    assert begin == BEGIN_TOKEN
    node, idx = compound(src, idx)
    end, idx = find_token(src, idx)
    assert end == END_TOKEN
    dot, idx = find_token(src, idx)
    assert dot == DOT_TOKEN
    prognode = ProgramNode(compound)
    return node



def nodevisitor(node):
    if isinstance(node, ProgramNode):
        nodevisitor(node.node)
    elif isinstance(node, CompundNode):
        print(node.intnode.value)







if __name__ == '__main__':
    pass

    idx = 0
    src = """
    BEGIN
    123
    END.
    """
    nodevisitor(program(src, idx))

"""
program: BEGIN compound END DOT
compound: PASS
"""
LETTERS = 'abcdefghijklmnopqurstuvwtxyz' + 'ABCDEFGHIJKLMNOPQURSTUVWTXYZ'
WHITESPACE = ' \n\t'


BEGIN = 'BEGIN'
END = 'END'
DOT_SYMBOL = '.'
DOT = 'DOT'
EOF = 'EOF'


EOF_TOKEN = (EOF, EOF)
BEGIN_TOKEN = (BEGIN, BEGIN)
END_TOKEN = (END, END)
DOT_TOKEN = (DOT, DOT)


is_idx_eof = lambda x, y: y == len(x)


class ProgramNode:
    def __init__(self, node):
        self.node = node

class CompundNode:
    pass



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

    else:
        raise Exception('CAN`T FIND TOKEN')

    return token, idx



def compound(src, idx):
    node = CompundNode()
    return node, idx



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
        pass






if __name__ == '__main__':
    pass

    idx = 0
    src = """
    BEGIN
    END.
    """
    nodevisitor(program(src, idx))

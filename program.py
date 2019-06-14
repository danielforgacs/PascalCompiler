LETTERS = 'abcdefghijklmnopqurstuvwtxyz' + 'ABCDEFGHIJKLMNOPQURSTUVWTXYZ'
DIGITS = '0123456789'
WHITESPACE = ' \n\t'


BEGIN = 'BEGIN'
END = 'END'
DOT_SYMBOL = '.'
DOT = 'DOT'
EOF = 'EOF'
SEMI_SYMBOL = ';'
SEMI = 'SEMI'

INTEGER = 'INTEGER'


EOF_TOKEN = (EOF, EOF)
BEGIN_TOKEN = (BEGIN, BEGIN)
END_TOKEN = (END, END)
DOT_TOKEN = (DOT, DOT_SYMBOL)
SEMI_TOKEN = (SEMI, SEMI_SYMBOL)


is_idx_eof = lambda x, y: y == len(x)



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

    elif char == SEMI_SYMBOL:
        token = SEMI_TOKEN
        idx += len(SEMI_SYMBOL)

    else:
        raise Exception('CAN`T FIND TOKEN')

    return token, idx



def peek_token(src, idx):
    token, _ = find_token(src, idx)
    return token



"""
program: BEGIN compound END DOT
compound: BEGIN END
"""

class CompoundNode(object):
    def __init__(self):
        self.nodes = []


def compound(src, idx):
    begin, idx = find_token(src, idx)
    assert begin == BEGIN_TOKEN

    if peek_token(src, idx) == BEGIN_TOKEN:
        node, idx = compound(src, idx)

    end, idx = find_token(src, idx)
    assert end == END_TOKEN

    return src, idx


def program(src, idx):
    compounds = CompoundNode()

    begin, idx = find_token(src, idx)
    assert begin == BEGIN_TOKEN

    while peek_token(src, idx) == BEGIN_TOKEN:
        node, idx = compound(src, idx)
        compounds.nodes.append(node)

    end, idx = find_token(src, idx)
    assert end == END_TOKEN
    dot, idx = find_token(src, idx)
    assert dot == DOT_TOKEN

    return node



def nodevisitor(node):
    pass



if __name__ == '__main__':
    pass

    src = """
BEGIN
    BEGIN
        BEGIN
            BEGIN
                BEGIN
                    BEGIN
                        BEGIN
                            BEGIN
                            END
                        END
                    END
                END
            END
        END
    END
    BEGIN
        BEGIN
        END
    END
    BEGIN
        BEGIN
            BEGIN
            END
        END
    END
    BEGIN
        BEGIN
        END
    END
END.
"""
    nodevisitor(program(src, 0))

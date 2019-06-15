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

    # print('::%s:%s::' % (token, idx))
    return token, idx


def peek_token(src, idx):
    token, _ = find_token(src, idx)
    return token[0]


"""
program:    BEGIN END DOT
            | SEMI factor
            | factor
factor: INTEGER
"""


class IntegerNode:
    def __init__(self, value):
        self.value = value

class ListNode:
    def __init__(self):
        self.nodes = []



def factor(src, idx):
    integertoken, idx = find_token(src, idx)
    node = IntegerNode(integertoken[1])

    return node, idx


def program(src, idx):
    nodelist = ListNode()

    begin, idx = find_token(src, idx)
    assert begin == BEGIN_TOKEN

    while True:
        intnode, idx = factor(src, idx)
        assert isinstance(intnode, IntegerNode), (intnode, idx)
        nodelist.nodes.append(intnode)
        if peek_token(src, idx) == SEMI:
            semi, idx = find_token(src, idx)
        else:
            break

    end, idx = find_token(src, idx)
    assert end == END_TOKEN, (end, idx)
    dot, idx = find_token(src, idx)
    assert dot == DOT_TOKEN, (dot, idx)
    eof, idx = find_token(src, idx)
    assert eof == EOF_TOKEN, (eof, idx)

    return nodelist, idx




def nodevisitor(node):
    if isinstance(node, IntegerNode):
        print(node.value)
    elif isinstance(node, ListNode):
        for item in node.nodes:
            nodevisitor(item)
    else:
        raise Exception('UNKNOWN NODE')



def interpreter(src):
    root, _ = program(src, 0)
    nodevisitor(root)





if __name__ == '__main__':
    pass

    src = """
BEGIN
    123;
    234;

    12211212; 873
END.
    """
    interpreter(src)


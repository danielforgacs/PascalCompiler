DIGITS = '0123456789'

EOF = 'EOF'
INTEGER = 'INTEGER'
PLUS_SYMBOL = '+'
PLUS = 'PLUS'
L_PAREN_SYMBOL = '('
L_PAREN = 'L_PAREN'
R_PAREN_SYMBOL = ')'
R_PAREN = 'R_PAREN'



class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value


class IntNode:
    def __init__(self, value):
        self.value = value



def find_integer(src, idx):
    numstr = src[idx]
    while True:
        idx += 1
        if idx == len(src):
            break
        if src[idx] not in DIGITS:
            break
        numstr += src[idx]
    num = int(numstr)
    return num, idx



def find_token(src, idx):
    if idx == len(src):
        token = Token(EOF, EOF)
        return token, idx

    char = src[idx]

    if char in DIGITS:
        num, idx = find_integer(src, idx)
        token = Token(INTEGER, num)

    elif char == PLUS_SYMBOL:
        token = Token(PLUS, PLUS_SYMBOL)
        idx += len(PLUS_SYMBOL)

    elif char == L_PAREN_SYMBOL:
        token = Token(L_PAREN, L_PAREN_SYMBOL)
        idx += len(L_PAREN_SYMBOL)

    elif char == R_PAREN_SYMBOL:
        token = Token(R_PAREN, R_PAREN_SYMBOL)
        idx += len(R_PAREN_SYMBOL)

    return token, idx


# factor: INTEGER | L_PAREN factor R_PAREN


def factor(src, idx):
    token, idx = find_token(src, idx)
    node = IntNode(token.value)

    if token.type_ == L_PAREN:
        node, idx = factor(src, idx)
        rparen, idx = find_token(src, idx)

    return node, idx

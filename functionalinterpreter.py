"""
expr: factor ((PLUS|MINUS) factor)*
factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT

-----------------------------
plus: '+'
minus: '-'
paren_left: '('
paren_right: ')'
integer: (0|1||3|4|5|6|7|8|9)*
"""

DIGITS = '0123456789'
WHITESPACE = ' '

# Tokens:
EOF = 'EOF'
INTEGER = 'INTEGER'
PLUS = '+'
MINUS = '-'
PAREN_LEFT = '('
PAREN_RIGHT = ')'




class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        # print(self)
    def __repr__(self):
        return '<%s:%s>' % (self.type_, self.value)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def find_integer(src, idx):
    result = ''
    while True:
        if idx == len(src):
            break
        if src[idx] in DIGITS:
            result += src[idx]
            idx += 1
        else:
            break
    number = int(result)
    return number, idx


def skip_whitespace(src, idx):
    while True:
        if idx == len(src):
            break
        if src[idx] != WHITESPACE:
            break
        else:
            idx += 1
    return idx


def find_token(src, idx):
    idx = skip_whitespace(src, idx)

    if idx == len(src):
        token = Token(EOF, EOF)
    elif src[idx] in DIGITS:
        number, idx = find_integer(src, idx)
        token = Token(INTEGER, number)
    elif src[idx] == PLUS:
        token = Token(PLUS, PLUS)
        idx += 1
    elif src[idx] == MINUS:
        token = Token(MINUS, MINUS)
        idx += 1
    elif src[idx] == PAREN_LEFT:
        token = Token(PAREN_LEFT, PAREN_LEFT)
        idx += 1
    elif src[idx] == PAREN_RIGHT:
        token = Token(PAREN_RIGHT, PAREN_RIGHT)
        idx += 1
    else:
        raise Exception('BAD CHAR FOR TOKEN: "%s", %s' % (src[idx], idx))

    return token, idx




def factor(src, idx):
    """
    factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT
    """
    token, idx = find_token(src, idx)

    if token.type_ == INTEGER:
        value = token.value
    elif token.type_ == PAREN_LEFT:
        value, idx = expr(src, idx)
    else:
        raise Exception('BAD FACTOR TOKEN: %s, %s' % (token, idx))

    return value, idx




def expr(src, idx):
    """
    expr: factor ((PLUS|MINUS) factor)*
    """
    value, idx = factor(src, idx)
    token, idx = find_token(src, idx)

    while token.type_ in [PLUS, MINUS]:
        right, idx = factor(src, idx)
        if token.type_ == PLUS:
            value += right
        elif token.type_ == MINUS:
            value -= right
        token, idx = find_token(src, idx)

    return value, idx




if __name__ == '__main__':
    pass

    print('--------------------')
    print(expr('(1)', 0))
    print('--------------------')
    print(expr('(1+1', 0))
    print('--------------------')
    print(expr('(1+1)+1', 0))

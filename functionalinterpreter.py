"""
expr: term ((PLUS|MINUS) term)*
term: factor ((MULT|DIV) factor)*
factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT



((INTEGER PLUS INTEGER))
((10+2))

PAREN_LEFT
    PAREN_LEFT
        INTEGER
        PLUS
        INTEGER
    PAREN_RIGHT
PAREN_RIGHT

-----------------------------
plus: '+'
minus: '-'
mult: '*'
div: '/'
paren_left: '('
paren_right: ')'
integer: (0|1||3|4|5|6|7|8|9)*
"""

DIGITS = '0123456789'
WHITESPACE = ' '

# Tokens:
EOF = 'EOF'
INTEGER = 'INTEGER'

PLUS_SYMBOL = '+'
PLUS = 'PLUS'
MINUS_SYMBOL = '-'
MINUS = 'MINUS'
MULT_SYMBOL = '*'
MULT = 'MULT'
DIV_SYMBOL = '/'
DIV = 'DIV'
PAREN_LEFT_SYMBOL = '('
PAREN_LEFT = 'PAREN_LEFT'
PAREN_RIGHT_SYMBOL = ')'
PAREN_RIGHT = 'PAREN_RIGHT'





class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        print(self)
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
        if len(src) == idx:
            break
        if src[idx] == WHITESPACE:
            idx += 1
        else:
            break
    return idx


def find_token(src, idx):
    idx = skip_whitespace(src, idx)

    if len(src) == idx:
        token = Token(EOF, EOF)
    elif src[idx] in DIGITS:
        number, idx = find_integer(src, idx)
        token = Token(INTEGER, number)
    elif src[idx] == PLUS_SYMBOL:
        token = Token(PLUS, PLUS_SYMBOL)
        idx += 1
    elif src[idx] == MINUS_SYMBOL:
        token = Token(MINUS, MINUS_SYMBOL)
        idx += 1
    elif src[idx] == PAREN_LEFT_SYMBOL:
        token = Token(PAREN_LEFT, PAREN_LEFT_SYMBOL)
        idx += 1
    elif src[idx] == PAREN_RIGHT_SYMBOL:
        token = Token(PAREN_RIGHT, PAREN_RIGHT_SYMBOL)
        idx += 1
    elif src[idx] == MULT_SYMBOL:
        token = Token(MULT, MULT_SYMBOL)
        idx += 1
    elif src[idx] == DIV_SYMBOL:
        token = Token(DIV, DIV_SYMBOL)
        idx += 1
    else:
        raise Exception('BAD CHAR FOR TOKEN: "%s", %s' % (src[idx], idx))

    return token, idx




def factor(src, idx):
    """
    expr: term ((PLUS|MINUS) term)*
    term: factor ((MULT|DIV) factor)*
    factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT
    """
    token, idx = find_token(src, idx)

    if token.type_ == INTEGER:
        value = token.value
    elif token.type_ == PAREN_LEFT:
        value, idx = expr(src, idx)
        token, idx = find_token(src, idx)
    else:
        raise Exception('BAD FACTOR TOKEN: %s, %s' % (token, idx))

    return value, idx




def term(src, idx):
    """
    expr: term ((PLUS|MINUS) term)*
    term: factor ((MULT|DIV) factor)*
    factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT
    """
    value, idx = factor(src, idx)

    while True:
        token, idx = find_token(src, idx)

        if token.type_ not in [MULT, DIV]:
            break

        right, idx = factor(src, idx)

        if token.type_ == MULT:
            value *= right
        elif token.type_ == DIV:
            value /= right

    return value, idx




def expr(src, idx):
    """
    expr: term ((PLUS|MINUS) term)*
    term: factor ((MULT|DIV) factor)*
    factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT
    """
    value, idx = term(src, idx)

    while True:
        token, idx = find_token(src, idx)

        if token.type_ not in [PLUS, MINUS]:
            break

        right, idx = term(src, idx)

        if token.type_ == PLUS:
            value += right
        elif token.type_ == MINUS:
            value -= right

    return value, idx




if __name__ == '__main__':
    pass

    print('--------------------')
    print(expr('10', 0))
    print('--------------------')
    print(expr('(10)', 0))
    print('--------------------')
    print(expr('(10+20)', 0))
    print('--------------------')
    print(expr('10+20', 0))
    print('--------------------')
    print(expr('1+2', 0))
    print('--------------------')
    print(expr('(((1+2)))', 0))

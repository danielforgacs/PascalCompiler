"""
expr: factor (PLUS|MINUS)*
factor: INTEGER

-----------------------------
plus: '+'
minus: '-'
integer: (0|1||3|4|5|6|7|8|9)*
"""

DIGITS = '0123456789'
WHITESPACE = ' '

# Tokens:
EOF = 'EOF'
INTEGER = 'INTEGER'
PLUS = '+'
MINUS = '-'




class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
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
    else:
        raise Exception('BAD CHAR FOR TOKEN: "%s", %s' % (src[idx], idx))

    return token, idx




def factor(src, idx):
    """
    factor: INTEGER
    """
    token, idx = find_token(src, idx)

    if token.type_ != INTEGER:
        raise Exception('BAD FACTOR TOKEN: %s, %s' % (token, idx))

    return token.value, idx




def expr(src, idx):
    """
    expr: factor (PLUS|MINUS)*
    """
    value, idx = factor(src, idx)
    token, idx = find_token(src, idx)

    if token.type_ == PLUS:
        result, idx  = expr(src, idx)
        value += result

    elif token.type_ == MINUS:
        result, idx  = expr(src, idx)
        value -= result

    elif token.type_ == EOF:
        pass

    else:
        raise Exception('BAD EXPR TOKEN: %s, %s' % (token, idx))

    return value, idx


# print(expr('1+1', 0))


# def find_token(src, idx):
#     src, idx = skip_whitespace(src, idx)

#     if idx == len(src):
#         return Token(EOF, EOF), idx

#     if src[idx] in DIGITS:
#         number, idx = find_integer(src, idx)
#         token = Token(INTEGER, number)

#     elif src[idx] == PLUS:
#         token = Token(PLUS, PLUS)
#         idx += 1

#     elif src[idx] == MINUS:
#         token = Token(MINUS, MINUS)
#         idx += 1

#     elif src[idx] == PAREN_LEFT:
#         token = Token(PAREN_LEFT, PAREN_LEFT)
#         idx += 1

#     elif src[idx] == PAREN_RIGHT:
#         token = Token(PAREN_RIGHT, PAREN_RIGHT)
#         idx += 1

#     else:
#         raise Exception('UNEXPECTED CHARACTER: %s' % src[idx])

#     return token, idx


# def eat(type_, src, idx):
#     token, idx = find_token(src, idx)

#     if token.type_ == type_:
#         return token.value, idx

#     else:
#         raise Exception('UNEXPECTED TOKEN: %s, idx: %s' % (token, idx))


# def factor(src, idx):
#     token, idx = find_token(src, idx)

#     if token.type_ == INTEGER:
#         return token.value, idx

#     elif token.type_ == PAREN_LEFT:
#         value, idx = expr(src, idx)
#         # token, idx = eat(PAREN_RIGHT, src, idx)
#         return value, idx

#     else:
#         raise Exception('FACTOR TOKEN ERROR: %s' % token)



# def expr(src, idx=0):
#     if len(src) == 0:
#         return None, idx

#     while True:
#         token, idx = find_token(src, idx)

#         if token.type_ == EOF:
#             break

#         elif token.type_ == INTEGER:
#             value = token.value

#         elif token.type_ == PLUS:
#             result, idx = factor(src, idx)
#             value += result

#         elif token.type_ == MINUS:
#             result, idx = factor(src, idx)
#             value -= result

#     return value, idx



if __name__ == '__main__':
    pass

LETTERS = 'abcdefghijklmnopqurstuvwtxyz' + 'ABCDEFGHIJKLMNOPQURSTUVWTXYZ'
DIGITS = '0123456789'
WHITESPACE = ' \n\t'


BEGIN = 'BEGIN'
END = 'END'
EOF = 'EOF'
INTEGER = 'INTEGER'


DOT_SYMBOL, DOT = '.', 'DOT'
SEMI_SYMBOL, SEMI = ';', 'SEMI'
PLUS_SYMBOL, PLUS = '+', 'PLUS'
MINUS_SYMBOL, MINUS = '-', 'MINUS'
MULT_SYMBOL, MULT = '*', 'MULT'
DIV_SYMBOL, DIV = '/', 'DIV'
L_PAREN_SYMBOL, L_PAREN = '(', 'LPAREN'
R_PAREN_SYMBOL, R_PAREN = ')', 'RPAREN'


BEGIN_TOKEN = (BEGIN, BEGIN)
END_TOKEN = (END, END)
EOF_TOKEN = (EOF, EOF)


DOT_TOKEN = (DOT, DOT_SYMBOL)
SEMI_TOKEN = (SEMI, SEMI_SYMBOL)
PLUS_TOKEN = (PLUS, PLUS_SYMBOL)
MINUS_TOKEN = (MINUS, MINUS_SYMBOL)
MULT_TOKEN = (MULT, MULT_SYMBOL)
DIV_TOKEN = (DIV, DIV_SYMBOL)
L_PAREN_TOKEN = (L_PAREN, L_PAREN_SYMBOL)
R_PAREN_TOKEN = (R_PAREN, R_PAREN_SYMBOL)


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

    elif char == PLUS_SYMBOL:
        token = PLUS_TOKEN
        idx += len(PLUS_SYMBOL)

    elif char == MINUS_SYMBOL:
        token = MINUS_TOKEN
        idx += len(MINUS_SYMBOL)

    elif char == MULT_SYMBOL:
        token = MULT_TOKEN
        idx += len(MULT_SYMBOL)

    elif char == DIV_SYMBOL:
        token = DIV_TOKEN
        idx += len(DIV_SYMBOL)

    elif char == L_PAREN_SYMBOL:
        token = L_PAREN_TOKEN
        idx += len(L_PAREN_SYMBOL)

    elif char == R_PAREN_SYMBOL:
        token = R_PAREN_TOKEN
        idx += len(L_PAREN_SYMBOL)

    else:
        raise Exception('CAN`T FIND TOKEN')

    return token, idx




def peek_token(src, idx):
    token, _ = find_token(src, idx)
    return token




"""
term: expr ((PLUL | MINUS) expr)*
expr: factor ((MULT | DIV) factor)*
factor: INTEGER | L_PAREN expr R_PAREN
"""




def factor(src, idx):
    nexttoken = peek_token(src, idx)

    if nexttoken[0] == INTEGER:
        token, idx = find_token(src, idx)
        value = token[1]

    elif nexttoken == L_PAREN_TOKEN:
        lparen, idx = find_token(src, idx)
        value, idx = term(src, idx)
        rparen, idx = find_token(src, idx)
        assert rparen == R_PAREN_TOKEN, rparen

    return value, idx





def expr(src, idx):
    value, idx = factor(src, idx)

    while peek_token(src, idx) in [MULT_TOKEN, DIV_TOKEN]:
        op, idx = find_token(src, idx)
        rightvalue, idx = factor(src, idx)

        if op == MULT_TOKEN:
            value *= rightvalue
        else:
            value /= rightvalue

    return value, idx




def term(src, idx):
    value, idx = expr(src, idx)

    while peek_token(src, idx) in [PLUS_TOKEN, MINUS_TOKEN]:
        op, idx = find_token(src, idx)
        rightvalue, idx = expr(src, idx)

        if op == PLUS_TOKEN:
            value += rightvalue
        else:
            value -= rightvalue

    return value, idx







if __name__ == '__main__':
    pass

    idx = 0
    src = """2*24+2+4+100+10-25-50+75*4/2"""
    src = """((2)+3)*(2+3)+2*24+2+4+100+10-25-50+75*(4/2)"""

    print(src)
    print('-'*79)

    token, _ = term(src, idx)
    print(token)
    print(eval(src))

    print('-'*79)

    while True:
        try:
            token, idx = find_token(src, idx)
            print(token[0].ljust(10), token[1])
        except Exception as error:
            break

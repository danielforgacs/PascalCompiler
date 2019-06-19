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


BEGIN_TOKEN = (BEGIN, BEGIN)
END_TOKEN = (END, END)
EOF_TOKEN = (EOF, EOF)


DOT_TOKEN = (DOT, DOT_SYMBOL)
SEMI_TOKEN = (SEMI, SEMI_SYMBOL)
PLUS_TOKEN = (PLUS, PLUS_SYMBOL)
MINUS_TOKEN = (MINUS, MINUS_SYMBOL)


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

    else:
        raise Exception('CAN`T FIND TOKEN')

    return token, idx




def peek_token(src, idx):
    token, _ = find_token(src, idx)
    return token[0]




"""
term: factor (PLU   )
factor: INTEGER
"""




def factor(src, idx):
    integertoken, idx = find_token(src, idx)

    return integertoken, idx







if __name__ == '__main__':
    pass

    idx = 0
    src = """
24
"""


    while True:
        try:
            token, idx = factor(src, idx)
            print(token)
        except Exception as error:
            break

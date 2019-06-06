DIGITS = '0123456789'

EOF = 'EOF'
INTEGER = 'INTEGER'
PLUS_SYMBOL = '+'
PLUS = 'PLUS'



class Token:
    def __init__(self, toktype, tokvalue):
        self.toktype = toktype
        self.tokvalue = tokvalue



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

    return token, idx



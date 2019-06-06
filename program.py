DIGITS = '0123456789'

EOF = 'EOF'
INTEGER = 'INTEGER'



class Token:
    def __init__(self, toktype, tokvalue):
        self.toktype = toktype
        self.tokvalue = tokvalue



def find_token(src, idx):
    if idx == len(src):
        token = Token(EOF, EOF)
        return token, idx

    char = src[idx]

    if char in DIGITS:
        token = Token(INTEGER, int(char))
        idx += 1

    return token, idx

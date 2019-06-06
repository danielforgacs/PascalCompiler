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

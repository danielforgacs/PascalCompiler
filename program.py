EOF = 'EOF'



class Token:
    def __init__(self, toktype, tokvalue):
        self.toktype = toktype
        self.tokvalue = tokvalue



def find_token(src, idx):
    return Token(EOF, EOF)

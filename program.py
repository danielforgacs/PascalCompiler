EOF = 'EOF'



class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value



def find_token(src, idx):
    return Token(EOF, EOF)

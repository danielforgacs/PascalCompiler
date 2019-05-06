"""
EXPR: FACTOR
FACTOR: INTEGER
"""


EOF = 'EOF'
INTEGER = 'INTEGER'



class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        return '<%s:%s>' % (self.type_, self.value)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__


def integer(src, idx):
    return 1


def find_token(src, idx):
    token = Token(EOF, EOF)

    while idx < len(src):
        if src[idx] in '0123456789':
            token = Token(INTEGER, integer(src, idx))
        else:
            raise Exception('UNEXPECTED CHARACTER')
        idx += 1

    return token, idx


def eat(type_, src, idx):
    token = find_token(src, idx)
    if token.type_ == type_:
        return token
    else:
        raise Exception('UNEXPECTED TOKEN')


def factor(src, idx):
    result = eat(INTEGER, src, idx)
    return result, idx


def expr(src, idx=0):
    result, idx = factor(src, idx)



if __name__ == '__main__':
    pass


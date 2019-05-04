INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULT = 'MULT'
DIV = 'DIV'
PAREN_LEFT = '('
PAREN_RIGHT = ')'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
    def __repr__(self):
        return '[%s][%s]' % (self.type_, self.value)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__



def integer(src, idx):
    result = ''

    while True:
        result += src[idx]
        idx += 1

        if idx == len(src):
            break

        if not src[idx] in '0123456789':
            break

    return int(result), idx



def skip_whitespace(src, idx):
    while True:
        if src[idx] != ' ':
            break
        idx += 1

        if idx == len(src):
            break

    return idx


def get_next_token(src, idx):
    if idx == len(src):
        return Token(EOF, EOF), idx

    idx = skip_whitespace(src, idx)

    if idx == len(src):
        return Token(EOF, EOF), idx

    char = src[idx]

    if char in '0123456789':
        number, idx = integer(src, idx)
        token = Token(INTEGER, number)

    elif char in '+':
        idx += 1
        token = Token(PLUS, '+')

    elif char in '-':
        idx += 1
        token = Token(MINUS, '-')

    elif char in '*':
        idx += 1
        token = Token(MULT, '*')

    elif char in '/':
        idx += 1
        token = Token(DIV, '/')

    else:
        raise Exception('CAN NOT GET NEXT TOKEN')

    # print('{:<5}{}'.format(idx, token))
    return token, idx



def term(src, idx):
    token, idx = get_next_token(src, idx)
    assert token.type_ == INTEGER
    result = token.value

    while True:
        idxin = idx
        token, idx = get_next_token(src=src, idx=idx)

        if token.type_ == MULT:
            number, idx = get_next_token(src, idx)
            result *= number.value

        elif token.type_ == DIV:
            number, idx = get_next_token(src, idx)
            result /= number.value

        else:
            idx = idxin
            break

    return result, idx




def expr(src, idx=0):
    if not src:
        return

    result, idx = term(src, idx)

    while True:
        idxin = idx
        token, idx = get_next_token(src=src, idx=idx)

        if token.type_ == PLUS:
            num, idx = term(src, idx)
            result += num

        elif token.type_ == MINUS:
            num, idx = term(src, idx)
            result -= num

        else:
            break

    return result


if __name__ == '__main__':
    pass

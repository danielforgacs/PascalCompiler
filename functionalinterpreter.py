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

    return src, idx


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

    elif char in '(':
        idx += 1
        token = Token(PAREN_LEFT, '(')

    elif char in ')':
        idx += 1
        token = Token(PAREN_RIGHT, ')')

    else:
        raise Exception('CAN NOT GET NEXT TOKEN')

    # print('{:<5}{}'.format(idx, token))
    return token, idx



def factor(src, idx):
    token, idx = get_next_token(src, idx)

    if token.type_ == INTEGER:
        return token.value, idx

    if token.type_ == PAREN_LEFT:
        # print(token)
        token, idx = get_next_token(src, idx)
        # print(token)

        result, idx = expr(src, idx)
        # token, idx = get_next_token(src, idx)
        # print(token)
        # assert token.type_ == PAREN_RIGHT, 'EXPECTED PAREN_RIGHT'
        return result, idx

        # token, _ = get_next_token(src, idx)
        # assert token.type_ == PAREN_RIGHT, 'MISSING CLOSING PAREN: %s' % idx

    # return result, idx



def term(src, idx):
    result, idx = factor(src, idx)

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
            # idx = idxin
            # print('BREAK')
            # print(result)
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

    # return result, idx
    return result, idx


if __name__ == '__main__':
    pass

    # print(expr('((1))')[0])
    # print(expr('((1+1))')[0])
    # print(expr('((1*1))')[0])
    # print(expr('((1/1))')[0])
    # print(expr('((1/1)+1)')[0])
    # print(expr('1+(1)')[0])
    # print(expr('1+(1+1)')[0])
    print(expr('1+')[0])
    # print(expr('1*(1+1)')[0])
    # print(expr('1*(1*1)')[0])

    # print(expr('1*(2+3)')[0])
    # print(expr('(1*(2+3))'))
    # print(expr('(1*(2+3))/1'))
    # print(expr('(1*(2+3))/1+(4+(5*6))'))
    # assert expr('(1*(2+3))/1+(4+(5*6))')


    # print(*expr('1'))
    # print(*expr('(1+1)'))
    # print(*expr('(1+1+2)'))
    # print(*expr('(1+1+2)+1'))
    # print(*expr('(1 +  1+2)+1'))
    # print(*expr('(1 +  1 +2  )+1'))
    # print(*expr('(1 +  1 +2  )   +   1'))
    # print(*expr('(1 +  1 +2  )   +   (1)'))

    # assert expr('1')[0] == 1
    # assert expr('(1)')[0] == 1
    # assert expr('((1))')[0] == 1
    # assert expr('(((1)))')[0] == 1
    # assert expr('((((1))))')[0] == 1
    # assert expr('((((1')[0] == 1
    # assert expr('1+1')[0] == 1+1
    # assert expr('(1+1)')[0] == (1+1)
    # assert expr('(1+(1))')[0] == (1+(1))
    # assert expr('(1+(1))')[0] == (1+(1))

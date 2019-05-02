INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULT = 'MULT'
DIV = 'DIV'
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



def exp(src, idx=0):
    if not src:
        return

    token, idx = get_next_token(src=src, idx=idx)
    result = token.value

    while True:
        print(token)
        token, idx = get_next_token(src=src, idx=idx)

        if token.type_ == PLUS:
            token, idx = get_next_token(src=src, idx=idx)
            result += token.value

        elif token.type_ == MINUS:
            token, idx = get_next_token(src=src, idx=idx)
            result -= token.value

        elif token.type_ == MULT:
            token, idx = get_next_token(src=src, idx=idx)
            result *= token.value

        elif token.type_ == DIV:
            token, idx = get_next_token(src=src, idx=idx)
            result /= token.value

        else:
            break

    return result


if __name__ == '__main__':
    pass

    assert not exp(src='')
    assert exp(src='3+5') == 3+5
    assert exp(src='0+0') == 0
    assert exp(src='9+9') == 9+9
    assert exp(src='100+100') == 100+100
    assert exp(src=' 3+5') == 3+5
    assert exp(src='    3+5') == 3+5
    assert exp(src='    3   +     5') == 3+5
    assert exp(src='3-5') == 3-5
    assert exp(src='0-0') == 0
    assert exp(src='9-9') == 9-9
    assert exp(src='100-100') == 100-100
    assert exp(src=' 3-5') == 3-5
    assert exp(src='    3-5') == 3-5
    assert exp(src='    3   -     5') == 3-5
    assert exp(src='12+23+34+25+16') == 12+23+34+25+16
    assert exp(src=' 12 + 23  + 34 + 25  + 16  ') == 12+23+34+25+16
    assert exp(src='1+1-1/1*1+1+1-1') == 1+1-1/1*1+1+1-1
    assert exp(src=' 1 + 1  - 1 / 1  *  1 + 1  +  1  - 1  ') == 1+1-1/1*1+1+1-1

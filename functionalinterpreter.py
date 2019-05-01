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
    while src[idx] == ' ':
        idx += 1
    return idx


def get_next_token(src, idx):
    idx = skip_whitespace(src, idx)
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

    print('{:<5}{}'.format(idx, token))
    return token, idx



def exp(src, idx=0):
    if not src:
        return

    left, idx = get_next_token(src=src, idx=idx)

    if not left.type_ == INTEGER:
        raise Exception('EXPRESSION LEFT ERROR')

    operator, idx = get_next_token(src=src, idx=idx)

    if not operator.type_ in [PLUS, MINUS, MULT, DIV]:
        raise Exception('EXPRESSION OP ERROR')

    right, idx = get_next_token(src=src, idx=idx)

    if not right.type_ == INTEGER:
        raise Exception('EXPRESSION RIGHT ERROR')

    if operator.type_ == PLUS:
        result = left.value + right.value
    elif operator.type_ == MINUS:
        result = left.value - right.value
    elif operator.type_ == MULT:
        result = left.value * right.value
    elif operator.type_ == DIV:
        result = left.value / right.value

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

INTEGER = 'INTEGER'
PLUS = 'PLUS'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value


def integer(src, idx):
    return int(src[idx]), idx+1


def get_next_token(src, idx):
    char = src[idx]

    if char in '0123456789':
        number, idx = integer(src, idx)
        return Token(INTEGER, int(char)), idx

    elif char in '+':
        idx += 1
        return Token(PLUS, PLUS), idx



def exp(src, idx=0):
    left, idx = get_next_token(src=src, idx=idx)

    if not left.type_ == INTEGER:
        raise

    operator, idx = get_next_token(src=src, idx=idx)

    if not operator.type_ == PLUS:
        raise Exception

    right, idx = get_next_token(src=src, idx=idx)

    if not right.type_ == INTEGER:
        raise

    result = left.value + right.value

    return result


if __name__ == '__main__':
    pass

    assert exp(src='3+5') == 3+5
    assert exp(src='0+0') == 0
    assert exp(src='9+9') == 9+9

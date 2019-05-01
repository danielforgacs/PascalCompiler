INTEGER = 'INTEGER'
PLUS = 'PLUS'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value


def get_next_token(src, idx):
    char = src[idx]

    if not char:
        return Token(EOF, EOF)

    elif char in '0123456789':
        return Token(INTEGER, int(char))

    elif char in '+':
        return Token(PLUS, PLUS)



def exp(src, idx=0):
    token = get_next_token(src=src, idx=idx)

    if not token.type_ == INTEGER:
        raise

    left = token
    idx += 1
    token = get_next_token(src=src, idx=idx)

    if not token.type_ == PLUS:
        raise

    operator = token
    idx += 1
    token = get_next_token(src=src, idx=idx)

    if not token.type_ == INTEGER:
        raise

    right = token

    result = left.value + right.value

    return result


if __name__ == '__main__':
    pass

    assert exp(src='3+5') == 3+5
    assert exp(src='0+0') == 0
    assert exp(src='9+9') == 9+9

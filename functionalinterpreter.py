"""
expr: term ((PLUS|MINUS) term)*
term: factor ((MULT|DIV) factor)*
factor: INTEGER | (PLUS|MINUS) factor | PAREN_LEFT expr PAREN_RIGHT


-----------------------------
plus: '+'
minus: '-'
mult: '*'
div: '/'
paren_left: '('
paren_right: ')'
integer: (0|1||3|4|5|6|7|8|9)*
"""

DIGITS = '0123456789'
WHITESPACE = ' '

# Tokens:
INTEGER = 'INTEGER'

EOF_SYMBOL = r'\0'
EOF = 'EOF'
PLUS_SYMBOL = '+'
PLUS = 'PLUS'
MINUS_SYMBOL = '-'
MINUS = 'MINUS'
MULT_SYMBOL = '*'
MULT = 'MULT'
DIV_SYMBOL = '/'
DIV = 'DIV'
PAREN_LEFT_SYMBOL = '('
PAREN_LEFT = 'PAREN_LEFT'
PAREN_RIGHT_SYMBOL = ')'
PAREN_RIGHT = 'PAREN_RIGHT'





class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        # print(self)
    def __repr__(self):
        return '<%s:%s>' % (self.type_, self.value)
    def __eq__(self, other):
        return self.__dict__ == other.__dict__






class BinOp(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right



class Num(object):
    def __init__(self, token):
        self.value = token.value
        self.token = token
    def __eq__(self, other):
        return self.__dict__ == other.__dict__





def find_integer(src, idx):
    result = ''
    while True:
        if idx == len(src):
            break
        if src[idx] in DIGITS:
            result += src[idx]
            idx += 1
        else:
            break
    number = int(result)
    return number, idx


def skip_whitespace(src, idx):
    while True:
        if len(src) == idx:
            break
        if src[idx] == WHITESPACE:
            idx += 1
        else:
            break
    return idx


def find_token(src, idx):
    idx = skip_whitespace(src, idx)

    if len(src) == idx:
        token = Token(EOF, EOF_SYMBOL)
        idx += 1
    elif src[idx] in DIGITS:
        number, idx = find_integer(src, idx)
        token = Token(INTEGER, number)
    elif src[idx] == PLUS_SYMBOL:
        token = Token(PLUS, PLUS_SYMBOL)
        idx += 1
    elif src[idx] == MINUS_SYMBOL:
        token = Token(MINUS, MINUS_SYMBOL)
        idx += 1
    elif src[idx] == PAREN_LEFT_SYMBOL:
        token = Token(PAREN_LEFT, PAREN_LEFT_SYMBOL)
        idx += 1
    elif src[idx] == PAREN_RIGHT_SYMBOL:
        token = Token(PAREN_RIGHT, PAREN_RIGHT_SYMBOL)
        idx += 1
    elif src[idx] == MULT_SYMBOL:
        token = Token(MULT, MULT_SYMBOL)
        idx += 1
    elif src[idx] == DIV_SYMBOL:
        token = Token(DIV, DIV_SYMBOL)
        idx += 1
    else:
        raise Exception('BAD CHAR FOR TOKEN: "%s", %s' % (src[idx], idx))

    return token, idx




def factor(src, idx):
    """
    expr: term ((PLUS|MINUS) term)*
    term: factor ((MULT|DIV) factor)*
    factor: INTEGER | (PLUS|MINUS) factor | PAREN_LEFT expr PAREN_RIGHT
    """
    token, idx = find_token(src, idx)

    if token.type_ == INTEGER:
        node = Num(token)
    elif token.type_ == PAREN_LEFT:
        node, idx = expr(src, idx)
        token, idx = find_token(src, idx)
        if token.type_ != PAREN_RIGHT:
            raise Exception('MISSING FACTOR PAREN_RIGHT: %s, %s' % (token, idx))
    else:
        raise Exception('BAD FACTOR TOKEN: %s, %s' % (token, idx))

    return node, idx




def term(src, idx):
    """
    expr: term ((PLUS|MINUS) term)*
    term: factor ((MULT|DIV) factor)*
    factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT
    """
    node, idx = factor(src, idx)

    while True:
        idx0 = idx
        token, idx = find_token(src, idx)

        if token.type_ not in [MULT, DIV]:
            idx = idx0
            break

        right, idx = factor(src, idx)
        node = BinOp(node, token, right)

    return node, idx




def expr(src, idx):
    """
    expr: term ((PLUS|MINUS) term)*
    term: factor ((MULT|DIV) factor)*
    factor: INTEGER | PAREN_LEFT expr PAREN_RIGHT
    """
    node, idx = term(src, idx)

    while True:
        idx0 = idx
        token, idx = find_token(src, idx)

        if token.type_ not in [PLUS, MINUS]:
            idx = idx0
            break

        right, idx = term(src, idx)
        node = BinOp(node, token, right)

    return node, idx



def parse(src):
    result, idx = expr(src, 0)
    return result




def nodevisitor(node):
    if isinstance(node, Num):
        return node.value

    elif isinstance(node, BinOp):
        if node.op.type_ == PLUS:
            return nodevisitor(node.left) + nodevisitor(node.right)
        elif node.op.type_ == MINUS:
            return nodevisitor(node.left) - nodevisitor(node.right)
        elif node.op.type_ == MULT:
            return nodevisitor(node.left) * nodevisitor(node.right)
        elif node.op.type_ == DIV:
            return nodevisitor(node.left) / nodevisitor(node.right)




def interpreter(src):
    result = nodevisitor(parse(src))
    return result



if __name__ == '__main__':
    pass

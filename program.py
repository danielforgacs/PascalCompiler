DIGITS = '0123456789'

EOF = 'EOF'
INTEGER = 'INTEGER'
PLUS_SYMBOL = '+'
PLUS = 'PLUS'
L_PAREN_SYMBOL = '('
L_PAREN = 'L_PAREN'
R_PAREN_SYMBOL = ')'
R_PAREN = 'R_PAREN'
SEMI_SYMBOL = ';'
SEMI = 'SEMI'



class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value


class IntNode:
    def __init__(self, value):
        self.value = value


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class StatementList:
    def __init__(self):
        self.nodes = []



def find_integer(src, idx):
    numstr = src[idx]
    while True:
        idx += 1
        if idx == len(src):
            break
        if src[idx] not in DIGITS:
            break
        numstr += src[idx]
    num = int(numstr)
    return num, idx



def find_token(src, idx):
    if idx == len(src):
        token = Token(EOF, EOF)
        return token, idx

    char = src[idx]

    if char in DIGITS:
        num, idx = find_integer(src, idx)
        token = Token(INTEGER, num)

    elif char == PLUS_SYMBOL:
        token = Token(PLUS, PLUS_SYMBOL)
        idx += len(PLUS_SYMBOL)

    elif char == L_PAREN_SYMBOL:
        token = Token(L_PAREN, L_PAREN_SYMBOL)
        idx += len(L_PAREN_SYMBOL)

    elif char == R_PAREN_SYMBOL:
        token = Token(R_PAREN, R_PAREN_SYMBOL)
        idx += len(R_PAREN_SYMBOL)

    elif char == SEMI_SYMBOL:
        token = Token(SEMI, SEMI_SYMBOL)
        idx += len(SEMI_SYMBOL)

    return token, idx


# statement: expr | SEMI expr
# expr: factor | (PLUS|MINUS) factor
# factor: INTEGER | L_PAREN expr R_PAREN


def factor(src, idx):
    token, idx = find_token(src, idx)
    node = IntNode(token.value)

    if token.type_ == L_PAREN:
        node, idx = expr(src, idx)
        rparen, idx = find_token(src, idx)

    return node, idx


def expr(src, idx):
    node, idx = factor(src, idx)
    idx0 = idx
    token, idx = find_token(src, idx)

    if token.type_ == PLUS:
        rigth, idx = factor(src, idx)
        node = BinOp(node.value, PLUS, rigth.value)
    else:
        idx = idx0

    return node, idx



def statement(src, idx):
    # statement: expr | SEMI expr
    root = StatementList()

    while True:
        node, idx = expr(src, idx)
        root.nodes.append(node)

        token, idx = find_token(src, idx)

        if token.type_ != SEMI:
            break

    # print(root.nodes)
    return root




def node_visitor(node):
    if isinstance(node, IntNode):
        print(node.value)
        # return node.value

    if isinstance(node, BinOp):
        if node.op == PLUS:
            print(node.left + node.right)
            # return node.left + node.right

    if isinstance(node, StatementList):
        # print(node)
        # print(node.nodes)
        # print(len(node.nodes))
        for node in node.nodes:
            # print('--', node)
            node_visitor(node)
            # return node_visitor(node)


def program(src):
    root = statement(src, 0)
    result = node_visitor(root)
    return result



if __name__ == '__main__':
    pass

    src = '1;2;3;4;5'
    src = '2+3;4+5'
    program(src)

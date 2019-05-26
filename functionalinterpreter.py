"""
program:                compound_statement DOT
compound_statement:     BEGIN statement_list END
statement_list:         statement | statement SEMI statement_list
statement:              compound_statement | assignment_statement | empty
assignment_statement:   variable ASSIGN expr
empty:
expr:                   term ((PLUS | MINUS) term)*
term:                   factor ((MUL | DIV) factor)*
factor:                 PLUS factor
                      | MINUS factor
                      | INTEGER
                      | LPAREN expr RPAREN
                      | variable
variable:               ID

-----------------------------
plus: '+'
minus: '-'
mult: '*'
div: '/'
paren_left: '('
paren_right: ')'
integer: (0|1||3|4|5|6|7|8|9)*
"""

WHITESPACE = [' ', '\n']
DIGITS = '0123456789'
ALPHA_CAPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHA_LOWER = 'abcdefghijklmnopqrstuvwxyz'

# Tokens:
INTEGER = 'INTEGER'
IDENTIFIER = 'IDENTIFIER'

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
SEMICOLON_SYMBOL = ';'
SEMICOLON = 'SEMICOLON'

DOT_SYMBOL = '.'
DOT = 'DOT'

BEGIN = 'BEGIN'
END = 'END'

ASSIGN_SYMBOL = ':='
ASSIGN = 'ASSIGN'

RESERVED_KEYWORDS = [
    BEGIN,
    END,
]





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





class UnaryOp(object):
    def __init__(self, op, token):
        self.op = op
        self.token = token




class Compound(object):
    def __init__(self):
        self.children = []



class Assign(object):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right


class Variable(object):
    def __init__(self, token):
        self.value = token.value
        self.token = token



class NoOp(object):
    pass



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


def find_text(src, idx):
    result = ''
    while True:
        if idx == len(src):
            break
        if src[idx] in ALPHA_CAPS + ALPHA_LOWER:
            result += src[idx]
            idx += 1
        else:
            break
    return result, idx


def skip_whitespace(src, idx):
    while src[idx] in WHITESPACE:
        idx += 1

        if idx == len(src):
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

    elif src[idx] in ALPHA_CAPS + ALPHA_LOWER:
        tokentext, idx = find_text(src, idx)
        token = Token(IDENTIFIER, tokentext)

        if tokentext in RESERVED_KEYWORDS:
            token = Token(tokentext, tokentext)

    elif src[idx] == ASSIGN_SYMBOL[0]:
        if idx < len(src):
            if src[idx+1] == ASSIGN_SYMBOL[1]:
                token = Token(ASSIGN, ASSIGN_SYMBOL)
                idx += len(ASSIGN_SYMBOL)

    elif src[idx] == PLUS_SYMBOL:
        token = Token(PLUS, PLUS_SYMBOL)
        idx += len(PLUS_SYMBOL)
    elif src[idx] == MINUS_SYMBOL:
        token = Token(MINUS, MINUS_SYMBOL)
        idx += len(MINUS_SYMBOL)
    elif src[idx] == PAREN_LEFT_SYMBOL:
        token = Token(PAREN_LEFT, PAREN_LEFT_SYMBOL)
        idx += len(PAREN_LEFT_SYMBOL)
    elif src[idx] == PAREN_RIGHT_SYMBOL:
        token = Token(PAREN_RIGHT, PAREN_RIGHT_SYMBOL)
        idx += len(PAREN_RIGHT_SYMBOL)
    elif src[idx] == MULT_SYMBOL:
        token = Token(MULT, MULT_SYMBOL)
        idx += len(MULT_SYMBOL)
    elif src[idx] == DIV_SYMBOL:
        token = Token(DIV, DIV_SYMBOL)
        idx += len(DIV_SYMBOL)
    elif src[idx] == DOT_SYMBOL:
        token = Token(DOT, DOT_SYMBOL)
        idx += len(DOT_SYMBOL)
    elif src[idx] == SEMICOLON_SYMBOL:
        token = Token(SEMICOLON, SEMICOLON_SYMBOL)
        idx += len(SEMICOLON_SYMBOL)

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
    elif token.type_ == PLUS:
        op = token
        token, idx = factor(src, idx)
        node = UnaryOp(op, token)
    elif token.type_ == MINUS:
        op = token
        token, idx = factor(src, idx)
        node = UnaryOp(op, token)
    else:
        node, idx = variable()

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




def program(src, idx):
    node, idx = compound_statement(src, idx)
    token, idx = find_token(src, idx)
    # assert token.type_ == DOT

    return node, idx




def compound_statement(src, idx):
    # breakpoint()
    token, idx = find_token(src, idx)
    # assert token.type_ == BEGIN

    nodes, idx = statement_list(src, idx)

    token, idx = find_token(src, idx)
    # assert token.type_ == END

    root = Compound()
    for node in nodes:
        root.children.append(node)

    return root, idx



def statement_list(src, idx):
# statement_list:         statement | statement SEMI statement_list
    node, idx = statement(src, idx)
    nodes = [node]

    while True:
        token, idx = find_token(src, idx)

        if token.type_ != SEMICOLON:
            break

        node, idx = statement()
        nodes.append(node)

    return nodes, idx




def statement(src, idx):
# statement: compound_statement | assignment_statement | empty
    token, idx = find_token(src, idx)

    if token.type_ == BEGIN:
        node, idx = compound_statement(src, idx)
    elif token.type_ == IDENTIFIER:
        node, idx = assignment_statement(src, idx)
    else:
        node = empty()

    return node, idx



def assignment_statement(src, idx):
# assignment_statement:   variable ASSIGN expr
    left, idx = variable(src, idx)
    token, idx = find_token(src, idx)
    right, idx = expr(src, idx)

    node = Assign(left, token, right)
    return node





def variable(src, idx):
    token, idx = find_token(src, idx)
    node = Variable(token)

    return node



def empty():
    return NoOp()






def parse(src):
    # breakpoint()
    result, idx = program(src, 0)
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

    elif isinstance(node, UnaryOp):
        if node.op.type_ == PLUS:
            return nodevisitor(node.token)
        elif node.op.type_ == MINUS:
            return nodevisitor(node.token) * -1




def interpreter(src):
    result = nodevisitor(parse(src))
    return result



if __name__ == '__main__':
    pass

    src = """
BEGIN
    BEGIN
        number := 2;
        a := number;
        b := 10 * a + 10 * number / 4;
        c := a - - b
    END;
    x := 11;
END.
"""
    print(parse(src))

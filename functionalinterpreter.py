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

WHITESPACE = ' '
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

    elif src[idx] in ALPHA_CAPS + ALPHA_LOWER:
        tokentext, idx = find_text(src, idx)
        token = Token(IDENTIFIER, tokentext)

        if tokentext in RESERVED_KEYWORDS:
            token = Token(tokentext, tokentext)


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

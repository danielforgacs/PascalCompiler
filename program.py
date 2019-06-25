LETTERS = 'abcdefghijklmnopqurstuvwtxyz' + 'ABCDEFGHIJKLMNOPQURSTUVWTXYZ'
DIGITS = '0123456789'
WHITESPACE = ' \n\t'


BEGIN = 'BEGIN'
END = 'END'
EOF = 'EOF'
INTEGER = 'INTEGER'


DOT_SYMBOL, DOT = '.', 'DOT'
SEMI_SYMBOL, SEMI = ';', 'SEMI'
PLUS_SYMBOL, PLUS = '+', 'PLUS'
MINUS_SYMBOL, MINUS = '-', 'MINUS'
MULT_SYMBOL, MULT = '*', 'MULT'
DIV_SYMBOL, DIV = '/', 'DIV'
L_PAREN_SYMBOL, L_PAREN = '(', 'LPAREN'
R_PAREN_SYMBOL, R_PAREN = ')', 'RPAREN'


BEGIN_TOKEN = (BEGIN, BEGIN)
END_TOKEN = (END, END)
EOF_TOKEN = (EOF, EOF)


DOT_TOKEN = (DOT, DOT_SYMBOL)
SEMI_TOKEN = (SEMI, SEMI_SYMBOL)
PLUS_TOKEN = (PLUS, PLUS_SYMBOL)
MINUS_TOKEN = (MINUS, MINUS_SYMBOL)
MULT_TOKEN = (MULT, MULT_SYMBOL)
DIV_TOKEN = (DIV, DIV_SYMBOL)
L_PAREN_TOKEN = (L_PAREN, L_PAREN_SYMBOL)
R_PAREN_TOKEN = (R_PAREN, R_PAREN_SYMBOL)


is_idx_eof = lambda x, y: y == len(x)





def find_identifier(src, idx):
    char = src[idx]
    result = char
    while True:
        idx += 1
        if is_idx_eof(src, idx):
            break
        char = src[idx]
        if char not in LETTERS:
            break
        result += char
    return result, idx





def find_integer(src, idx):
    result = src[idx]
    while True:
        idx += 1
        if is_idx_eof(src, idx):
            break
        if src[idx] not in DIGITS:
            break
        result += src[idx]

    number = int(result)
    return number, idx




def find_token(src, idx):
    if is_idx_eof(src, idx):
        idx += 1
        return EOF_TOKEN, idx

    char = src[idx]

    while char in WHITESPACE:
        idx += 1
        if is_idx_eof(src, idx):
            return EOF_TOKEN, idx
        char = src[idx]

    if char in LETTERS:
        identifier, idx = find_identifier(src, idx)

        if identifier == BEGIN:
            token = BEGIN_TOKEN
        elif identifier == END:
            token = END_TOKEN

    elif char == DOT_SYMBOL:
        token = DOT_TOKEN
        idx += len(DOT_SYMBOL)

    elif char in DIGITS:
        number, idx = find_integer(src, idx)
        token = (INTEGER, number)

    elif char == SEMI_SYMBOL:
        token = SEMI_TOKEN
        idx += len(SEMI_SYMBOL)

    elif char == PLUS_SYMBOL:
        token = PLUS_TOKEN
        idx += len(PLUS_SYMBOL)

    elif char == MINUS_SYMBOL:
        token = MINUS_TOKEN
        idx += len(MINUS_SYMBOL)

    elif char == MULT_SYMBOL:
        token = MULT_TOKEN
        idx += len(MULT_SYMBOL)

    elif char == DIV_SYMBOL:
        token = DIV_TOKEN
        idx += len(DIV_SYMBOL)

    elif char == L_PAREN_SYMBOL:
        token = L_PAREN_TOKEN
        idx += len(L_PAREN_SYMBOL)

    elif char == R_PAREN_SYMBOL:
        token = R_PAREN_TOKEN
        idx += len(L_PAREN_SYMBOL)

    else:
        raise Exception('CAN`T FIND TOKEN')

    return token, idx




def peek_token(src, idx):
    token, _ = find_token(src, idx)
    return token


# Nodes ---------------------------------------------------:


class NumNode:
    def __init__(self, token):
        self.value = token[1]


class UnaryOp:
    def __init__(self, op, node):
        self.op = op
        self.node = node


class BinOp:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op[0]
        self.right = right




"""
expr: term ((PLUS | MINUS) term)*
term: factor ((MULT | DIV) factor)*
factor: INTEGER | L_PAREN expr R_PAREN | (PLUS | MINUS) factor

----------------------------------------------------------------------------

program: compound_statement DOT
compound_statement: BEGIN statement_list END
statement_list: statement
                | statement SEMI statement_list
statement: compound_statement
           | assignment_statement
           | empty
assignment_statement: variable ASSIGN expr
empty:
expr: term ((PLUS | MINUS) term)*
term: factor ((MUL | DIV) factor)*
factor: PLUS factor
        | MINUS factor
        | INTEGER
        | LPAREN expr RPAREN
        | variable
variable: ID
"""



def variable(src, idx):
    """
    variable: ID
    """
    pass




def factor(src, idx):
    """
    factor: PLUS factor
            | MINUS factor
            | INTEGER
            | LPAREN expr RPAREN
            | variable
    """
    nexttoken = peek_token(src, idx)

    if nexttoken[0] == INTEGER:
        token, idx = find_token(src, idx)
        node = NumNode(token)

    elif nexttoken in [MINUS_TOKEN, PLUS_TOKEN]:
        op, idx = find_token(src, idx)
        operand, idx = factor(src, idx)
        node = UnaryOp(op, operand)

    elif nexttoken == L_PAREN_TOKEN:
        lparen, idx = find_token(src, idx)
        node, idx = expr(src, idx)
        rparen, idx = find_token(src, idx)
        assert rparen == R_PAREN_TOKEN, rparen

    return node, idx





def term(src, idx):
    """
    term: factor ((MUL | DIV) factor)*
    """

    node, idx = factor(src, idx)

    while peek_token(src, idx) in [MULT_TOKEN, DIV_TOKEN]:
        op, idx = find_token(src, idx)
        rightnode, idx = factor(src, idx)
        node = BinOp(node, op, rightnode)

    return node, idx




def expr(src, idx):
    node, idx = term(src, idx)

    while peek_token(src, idx) in [PLUS_TOKEN, MINUS_TOKEN]:
        op, idx = find_token(src, idx)
        rightvalue, idx = term(src, idx)
        node = BinOp(node, op, rightvalue)

    return node, idx



def empty(src, idx):
    pass



def assignment_statement(src, idx):
    """
    assignment_statement: variable ASSIGN expr
    """
    pass




def statement(src, idx):
    """
    statement: compound_statement
               | assignment_statement
               | empty
    """
    pass




def statement_list(src, idx):
    """
    statement_list: statement
                    | statement SEMI statement_list
    """
    pass




def compound_statement(src, idx):
    """
    compound_statement: BEGIN statement_list END
    """
    pass




def program(src, idx):
    """
    program: compound_statement DOT
    """
    pass






# AST -------------------------------------------------------------------------



def nodevisitor(node):
    if isinstance(node, NumNode):
        result = node.value

    elif isinstance(node, UnaryOp):
        if node.op == MINUS_TOKEN:
            result = 0 - nodevisitor(node.node)
        else:
            result = nodevisitor(node.node)

    elif isinstance(node, BinOp):
        if node.op == PLUS:
            result = nodevisitor(node.left) + nodevisitor(node.right)
        elif node.op == MINUS:
            result = nodevisitor(node.left) - nodevisitor(node.right)
        elif node.op == MULT:
            result = nodevisitor(node.left) * nodevisitor(node.right)
        elif node.op == DIV:
            result = nodevisitor(node.left) / nodevisitor(node.right)

    return result




def interprer(src):
    rootnode, _ = expr(src, 0)
    return nodevisitor(rootnode)





if __name__ == '__main__':
    pass

    idx = 0
    src = """2*24+2+4+100+10-25-50+75*4/2"""
    src = """((2)+3)*(2+--3)+2*24-+-+-+ +2+4+100+10-25-50+75*(4/2)"""
    # src = """-(1+1)"""
    src = """
    x
    """

    print(src)
    print('-'*79)

    interprer(src)
    # print(eval(src))

    # assert interprer(src) == eval(src), 'RESULT DOESN`T MATCH EVAL!'

    # print('-'*79)

    # while True:
    #     try:
    #         token, idx = find_token(src, idx)
    #         print(token[0].ljust(10), token[1])
    #     except Exception as error:
    #         break

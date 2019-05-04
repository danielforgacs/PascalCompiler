# Token types:
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULT = 'MULT'
DIV = 'DIV'
PAREN_LEFT = 'PAREN_LEFT'
PAREN_RIGHT = 'PAREN_RIGHT'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    def __repr__(self):
        return '[%s]:[%s]' % (self.type_, self.value)

    def __eq__(self, other):
        return (self.type_ == other.type_) and (self.value == other.value)



class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None
        self.current_char = None

        if text:
            self.current_char = self.text[self.pos]


    def advance(self):
        self.pos += 1

        if self.pos == len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]


    def skip_whitespace(self):
        while self.current_char and (self.current_char == ' '):
            self.advance()


    def integer(self):
        result = ''
        while (self.current_char is not None) and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)



    def get_next_token(self):
        token = None

        while self.current_char:
            if self.current_char == ' ':
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                token = Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                token = Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                token = Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                token = Token(MULT, '*')

            if self.current_char == '/':
                self.advance()
                token = Token(DIV, '/')

            if self.current_char == '(':
                self.advance()
                token = Token(PAREN_LEFT, '(')

            if self.current_char == ')':
                self.advance()
                token = Token(PAREN_RIGHT, ')')

            if not token:
                raise Exception('NEXT TOKEN ERROR')

            print(token)
            return token

        return Token(EOF, None)



class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            raise Exception('CAN NOT EAT')


    def factor(self):
        token = self.current_token

        if token.type_ == INTEGER:
            self.eat(INTEGER)
            return token.value

        elif token.type_ == PAREN_LEFT:
            self.eat(PAREN_LEFT)
            result = self.expr()
            self.eat(PAREN_RIGHT)
            return result



    def term(self):
        result = self.factor()

        while self.current_token.type_ in (MULT, DIV):
            if self.current_token.type_ == MULT:
                self.eat(MULT)
                result *= self.factor()
            elif self.current_token.type_ == DIV:
                self.eat(DIV)
                result /= self.factor()

        return result



    def expr(self):
        if self.current_token.type_ == EOF:
            return

        result = self.term()

        while self.current_token.type_ in (PLUS, MINUS):
            if self.current_token.type_ == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif self.current_token.type_ == MINUS:
                self.eat(MINUS)
                result -= self.term()

        return result


print(Interpreter(Lexer('(1)')).expr())
# print(1-1/1+1)

# Token types:
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
        return '[%s]:[%s]' % (self.type_, self.value)

    def __eq__(self, other):
        return (self.type_ == other.type_) and (self.value == other.value)



class Interpreter:
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
        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)


    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value


    def get_next_token(self):
        while self.current_char:
            if self.current_char == ' ':
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MULT, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            raise Exception('NEXT TOKEN ERROR')

        return Token(EOF, None)


    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.get_next_token()
        else:
            raise Exception('CAN NOT EAT')


    def exp(self):
        if not self.current_char:
            return

        self.current_token = self.get_next_token()

        result = self.term()

        while self.current_token.type_ in (PLUS, MINUS, MULT, DIV):
            token = self.current_token

            if token.type_ == PLUS:
                self.eat(PLUS)
                result += self.term()
            elif token.type_ == MINUS:
                self.eat(MINUS)
                result -= self.term()
            elif token.type_ == MULT:
                self.eat(MULT)
                result *= self.term()
            elif token.type_ == DIV:
                self.eat(DIV)
                result /= self.term()

        return result

# Token types:
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULT = 'MULT'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        # None, 0123456789, '+', '-'
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
        left = self.current_token
        self.eat(INTEGER)
        op = self.current_token

        if op.value == '+':
            self.eat(PLUS)
        elif op.value == '-':
            self.eat(MINUS)
        elif op.value == '*':
            self.eat(MULT)

        right = self.current_token
        self.eat(INTEGER)

        if op.type_ == PLUS:
            result = left.value + right.value
        elif op.type_ == MINUS:
            result = left.value - right.value
        elif op.type_ == MULT:
            result = left.value * right.value

        return result


# Token types:
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
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
        self.current_char = self.text[self.pos]


    def advance(self):
        self.pos += 1
        if self.pos == len(self.text):
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]


    def get_next_token(self):
        if self.pos > len(self.text)-1:
            return Token(EOF, None)

        char = self.text[self.pos]

        if char.isdigit():
            token = Token(INTEGER, int(char))
            self.pos += 1

            return token

        if char == '+':
            token = Token(PLUS, '+')
            self.pos += 1

            return token

        if char == '-':
            token = Token(MINUS, '-')
            self.pos += 1

            return token



        raise Exception('CAN`T GET TOKEN')


    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.get_next_token()
        else:
            raise Exception('CAN NOT EAT')


    def exp(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)
        op = self.current_token

        if op.value == '+':
            self.eat(PLUS)
        elif op.value == '-':
            self.eat(MINUS)

        right = self.current_token
        self.eat(INTEGER)

        if op.type_ == PLUS:
            result = left.value + right.value
        elif op.type_ == MINUS:
            result = left.value - right.value

        return result


# Token types:
INTEGER = 'INTEGER'
PLUS = 'PLUS'
EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        # None, 0123456789, '+'
        self.value = value

    def __repr__(self):
        return '[%s]:[%s]' % (self.type_, self.value)



class Interpreter:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def get_next_token(self):
        text = self.text

        if self.pos > len(text)-1:
            return Token(EOF, None)

        char = text[self.pos]

        if char.isdigit():
            token = Token(INTEGER, int(char))
            self.pos += 1

            return token

        if char == '+':
            token = Token(PLUS, '+')
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
        self.eat(PLUS)
        right = self.current_token
        self.eat(INTEGER)
        result = left.value + right.value
        return result


src = ''
interp = Interpreter(text=src)
result  = interp.exp()
assert result == 3+5

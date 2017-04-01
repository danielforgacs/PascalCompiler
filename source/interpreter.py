"""
token types:
EOF: indicates no more input
for lexical analysis
"""
INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
MULTIPLY = 'MULTIPLY'
DIVISION = 'DIVISION'
EOF = 'EOF'


def msg(txt, val=''):
    print('\t{}: {}'.format(txt, val))

class Token:
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value
        msg('token found:')
        msg(self)

    def __str__(self):
        self_string = (
            'Token:'
            '\ttype: {type_}'
            '\tvalue: {value}'.format(
            type_=self.type_,
            value=self.value,
            )
        )
        return self_string

    def __repr__(self):
        return self.__str__()


class Interpreter:
    def __init__(self, text):
        self.text = text
        # --> Index of self.text
        self.pos = 0
        self.current_token = None
        self.current_char = self.text[self.pos]

# ##########################
# --> LEXER
# ##########################

    def error(self):
        raise Exception('Error parsing code')


    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''

        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return int(result)


    def get_next_token(self):
        """
        Lexical analyzer / tokenizer
        breakes code into tokens
        """
        while self.current_char is not None:
            if self.current_char.isspace():
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
                return Token(MULTIPLY, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIVISION, self.current_char)

            self.error()

        return Token(EOF, None)


    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        """
        Perser / interpreter

        expr: INTEGER PLUS INTEGER
        expr: INTEGER MINUS INTEGER
        """
        self.current_token = self.get_next_token()

        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token

        if op.type_ == PLUS:
            self.eat(PLUS)
        elif op.type_ == MINUS:
            self.eat(MINUS)
        elif op.type_ == MULTIPLY:
            self.eat(MULTIPLY)
        elif op.type_ == DIVISION:
            self.eat(DIVISION)
        else:
            self.error()

        right = self.current_token
        self.eat(INTEGER)

        if op.type_ == PLUS:
            result = left.value + right.value
        elif op.type_ == MINUS:
            result = left.value - right.value
        elif op.type_ == MULTIPLY:
            result = left.value * right.value
        elif op.type_ == DIVISION:
            result = left.value / right.value

        else:
            self.error()

        return result



def main():
    msg('START')
    while True:
        try:
            text = input('calc >')
        except EOFError:
            break

        if not text:
            break

        msg('starting interpreter')
        interpreter = Interpreter(text)
        msg('interpreter expr()')
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
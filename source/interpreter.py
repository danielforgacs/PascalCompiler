"""
token types:
EOF: indicates no more input
for lexical analysis
"""
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


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('++> INVALID CHARACHTER')

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
        int_chars = ''

        while self.current_char and self.current_char.isdigit():
            int_chars += self.current_char
            self.advance()

        return int(int_chars)

    def get_next_token(self):
        while self.current_char:
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
                return Token(MULT, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
        print ('#'*8)
        print (type(self.lexer))
        print ('#'*8)
        self.current_token = self.lexer.get_next_token()

    def error(self):
        raise Exception('++> INVALID SYNTAX')

    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        result = self.factor()

        while self.current_token.type_ in (MULT, DIV):
            token = self.current_token

            if token.type_ == PLUS:
                self.eat(PLUS)
                result = result + self.factor()

            if token.type_ == MINUS:
                self.eat(MINUS)
                result = result - self.factor()

            if token.type_ == MULT:
                self.eat(MULT)
                result = result * self.factor()

            elif token.type_ == DIV:
                self.eat(DIV)
                result = result / self.factor()

        return result


def main():
    while True:
        try:
            text = input('calc >')
        except EOFError:
            break

        if not text:
            break

        lexer = Lexer(text)
        interpreter = Interpreter(lexer)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
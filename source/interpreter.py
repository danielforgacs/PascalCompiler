import pdb

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

# ##########################
# --> LEXER
# ##########################

    def error(self):
        raise Exception('++> INVALID CHARACHTER')


    def advance(self):
        self.pos += 1

        if self.pos > len(self.text) - 1:
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

<<<<<<< HEAD
    def skip_whitespace(self):
=======
    def skip(self):
>>>>>>> 2c551fe705ee6d0cf362b4ecfc801209d8616d60
        while self.current_char and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''

        while self.current_char and self.current_char.isdigit():
            result += self.current_char
            self.advance()

        return result

    def get_next_token(self):
        while self.current_char:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '*':
                self.advance()
                return Token(MULT, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)


<<<<<<< HEAD
# ##########################################
# --> PARSER
# ##########################################


    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.get_next_token()
            msg('eating current tokeb', self.current_token)
        else:
            self.error()


    def term(self):
        token = self.current_token
        self.eat(INTEGER)
        return token.value


    def expr(self):
        """
        Perser / interpreter

        expr: INTEGER PLUS INTEGER
        expr: INTEGER MINUS INTEGER
        """
        # pdb.set_trace()
        self.current_token = self.get_next_token()


        result = self.term()

        while self.current_token.type_ in (PLUS, MINUS, MULTIPLY, DIVISION):
            token = self.current_token
            msg('expression loop', token)

            if token.type_ == PLUS:
                self.eat(PLUS)
                result = result + self.term()

            elif token.type_ == MINUS:
                self.eat(MINUS)
                result = result - self.term()

            elif token.type_ == MULTIPLY:
                self.eat(MULTIPLY)
                result = result * self.term()

            elif token.type_ == DIVISION:
                self.eat(DIVISION)
                result = result / self.term()

            # else:
            #     break
=======
class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer
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

            if token.type_ == MULT:
                self.eat(MULT)
                result = result * self.factor()

            elif token.type_ == DIV:
                self.eat(DIV)
                result = result / self.factor()
>>>>>>> 2c551fe705ee6d0cf362b4ecfc801209d8616d60

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
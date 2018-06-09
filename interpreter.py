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


class Interpreter:
    def __init__(self, text):
        self.text =  text
        self.pos = 0
        self.currenttoken = None
        self.currentchar = self.text[self.pos]

    # def error(self):
    #     raise Exception('::: error parsing :::')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.currentchar = None
        else:
            self.currentchar = self.text[self.pos]

    def skip_whitespace(self):
        while self.currentchar and self.currentchar.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.currentchar and self.currentchar.isdigit():
            result += self.currentchar
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.currentchar:
            if self.currentchar.isspace():
                self.skip_whitespace()
                continue

            if self.currentchar.isdigit():
                return Token(type_=INTEGER, value=self.integer())

            if self.currentchar == '+':
                self.advance()
                return Token(type_=PLUS, value='+')

            if self.currentchar == '-':
                self.advance()
                return Token(type_=MINUS, value='-')

            if self.currentchar == '*':
                self.advance()
                return Token(type_=MULT, value='*')

            if self.currentchar == '/':
                self.advance()
                return Token(type_=DIV, value='/')

            # self.error()
            raise Exception('GET NEXT TOKEN ERROR!')

        return Token(type_=EOF, value=None)


    def eat(self, tokentype):
        if self.currenttoken.type_ != tokentype:
            # self.error()
            raise Exception('EAT ERROR!')
        self.currenttoken = self.get_next_token()


    def term(self):
        token = self.currenttoken
        self.eat(INTEGER)
        return token.value


    def expr(self):
        self.currenttoken = self.get_next_token()
        result = self.term()

        while self.currenttoken.type_ in (PLUS, MINUS, MULT, DIV):
            token = self.currenttoken

            if token.type_ == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type_ == MINUS:
                self.eat(MINUS)
                result = result - self.term()
            elif token.type_ == MULT:
                self.eat(MULT)
                result = result * self.term()
            elif token.type_ == DIV:
                self.eat(DIV)
                result = result / self.term()

        return result


def main():
    while True:
        try:
            text = input()
        except EOFError:
            break
        if not text:
            break

        interpreter = Interpreter(text=text)
        result = interpreter.expr()
        print(result)



if __name__ == '__main__':
    pass
    main()

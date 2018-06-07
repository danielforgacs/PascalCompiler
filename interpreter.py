INTEGER = 'INTEGER'
PLUS = 'PLUS'
MINUS = 'MINUS'
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

    def error(self):
        raise Exception('::: error parsing :::')

    def advance(self):
        self.pos += 1
        if self.pos > len(self.text)-1:
            self.currentchar = None
        else:
            self.currentchar = self.text[self.pos]

    def skip_whitespace(self):
        while self.currentchar and self.currentchar.isspace():
            self.advace()

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
                return Token(INTEGER, self.integer())

            if self.currentchar == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.currentchar == '-':
                self.advance()
                return Token(MINUS, '-')

            self.error()

        return Token(EOF, None)


    def eat(self, tokentype):
        if self.currenttoken.type_ != tokentype:
            self.error()
        self.currenttoken = self.get_next_token()


    def expr(self):
        self.currenttoken = self.get_next_token()
        left = self.currenttoken
        self.eat(INTEGER)
        op = self.currenttoken
        if op.type_ == 'PLUS':
            self.eat(PLUS)
        else:
            self.eat(MINUS)
        right = self.currenttoken
        self.eat(INTEGER)
        if op.type_ == 'PLUS':
            result = left.value + right.value
        else:
            result = left.value - right.value

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

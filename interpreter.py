INTEGER = 'INTEGER'
PLUS = 'PLUS'
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

    def error(self):
        raise Exception('::: error parsing :::')

    def get_next_token(self):
        text = self.text

        if self.pos > len(text)-1:
            return Token(type=EOF, value=None)

        currentchar = text[self.pos]

        if currentchar.isdigit():
            self.pos += 1
            return Token(type_=INTEGER, value=int(currentchar))

        elif currentchar == '+':
            self.pos += 1
            return Token(type_=PLUS, value=currentchar)

        else:
            self.error()




if __name__ == '__main__':
    pass

    interp = Interpreter('1+2')

    print(interp.get_next_token().value)
    print(interp.get_next_token().value)
    print(interp.get_next_token().value)

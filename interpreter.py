INTEGER = 'INTEGER'
PLUS = 'PLUS'
EOF = 'EOF'


class Token:
    def __init__(self, type, value):
        self.type = type
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


if __name__ == '__main__':
    pass


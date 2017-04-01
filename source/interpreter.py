"""
token types:
EOF: indicates no more input
for lexical analysis
"""
INTEGER = 'INTEGER'
PLUS = 'PLUS'
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

    def error(self):
        raise Exception('Error parsing code')

    def get_next_token(self):
        """
        Lexical analyzer / tokenizer
        breakes code into tokens
        """

        text = self.text
        print ('\t..text:', self.text)

        if self.pos > len(text) - 1:
            msg('EOF expression')
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char.isdigit():
            msg('digit found', current_char)
            token = Token(INTEGER, int(current_char))
            self.pos += 1
            return token

        if current_char == '+':
            token = Token(PLUS, current_char)
            self.pos += 1
            return token

        self.error()

    def eat(self, token_type):
        if self.current_token.type_ == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def expr(self):
        self.current_token = self.get_next_token()
        left = self.current_token
        self.eat(INTEGER)

        op = self.current_token
        self.eat(PLUS)

        right = self.current_token
        self.eat(INTEGER)

        result = left.value + right.value
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
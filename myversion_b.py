"""
"""

INT = 'INT'
LPAREN = '('
RPAREN = ')'
PLUS = '+'
MINUS = '-'
MUL = '*'
DIV = '/'



import pytest


class Token:
    def __init__(self, typ, value):
        self.typ = typ
        self.value = value


# def get_integer(text, pos):
#   result = ''
#   counter = pos

#   while text[counter] in '0123456789':
#       result += text[counter]
#       if counter == len(text)-1:
#           break
#       counter += 1

#   return Token(INT, int(result)), counter


def skip_space(text, pos):
    while text[pos] == ' ':
        pos += 1

    return pos





def get_next_token(source, pos):
    return pos


def calculator(source):
    """
    expr   : term ((PLUS | MINUS) term)*
    term   : factor ((MUL | DIV) factor)*
    factor : INTEGER | LPAREN expr RPAREN
    """
    pos = 0
    result = get_next_token(source=source, pos=pos)
    return ''



# def expr(text):
#     pos = 0
#     pos = skip_space(text=text, pos=pos)
#     token, pos = get_integer(text=text, pos=pos)
#     result = token.value

#     while pos < len(text)-1:
#         pos = skip_space(text=text, pos=pos)
#         op = text[pos]
#         pos += 1
#         pos = skip_space(text=text, pos=pos)
#         token, pos = get_integer(text=text, pos=pos)

#         if op == '+':
#             result += token.value
#         elif op == '-':
#             result -= token.value

#     return result


@pytest.mark.parametrize('kwargs, expected', (
    ({'text': 'a', 'pos': 0}, 0),
    ({'text': ' a', 'pos': 0}, 1),
    ({'text': '   a', 'pos': 0}, 3),
    ({'text': '   a', 'pos': 2}, 3),
    ({'text': 's   a', 'pos': 2}, 4),
    ))
def test_skip_space(kwargs, expected):
    pos = skip_space(**kwargs)
    assert pos == expected


@pytest.mark.parametrize('text, expected', (
    ('', ''),
    ))
def test_calculator(text, expected):
    assert calculator(source=text) == expected



if __name__ == '__main__':
    pass

    pytest.main([
        __file__,
    ])
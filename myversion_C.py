"""
1+2+3

INT ((+|-) INT)*
"""


import pytest


class Token:
	def __init__(self, typ, value):
		self.typ = typ
		self.value = value


def get_integer(text, pos):
	result = ''
	counter = pos

	while text[counter] in '0123456789':
		result += text[counter]
		if counter == len(text)-1:
			break
		counter += 1

	return Token('INT', int(result)), counter



def expr(text):
    pos = 0

    # while pos < len(text):
    token1, pos = get_integer(text=text, pos=pos)
    # pos += 1
    op = text[pos]
    pos += 1
    token2, pos = get_integer(text=text, pos=pos)

    return token1.value + token2.value 




@pytest.mark.parametrize('source, expected', (
    ('1+1', 1+1),
    ('11+1', 11+1),
    ('123+654', 123+654),
    ))
def test_expr_01(source, expected):
    assert expr(text=source) == expected
    






@pytest.mark.parametrize('text, expected', (
    ('1', ('INT', 1)),
    ('11', ('INT', 11)),
    ('11 ', ('INT', 11)),
    ('11 1', ('INT', 11)),
    ('2345', ('INT', 2345)),
    ))
def test_get_next_token_returns_tokens_from_pos(text, expected):
    token = get_integer(text=text, pos=0)[0]
    assert token.typ == Token(*expected).typ
    assert token.value == Token(*expected).value


if __name__ == '__main__':
    pass

    pytest.main([
        __file__,
        # '-v',
        '-s'
    ])
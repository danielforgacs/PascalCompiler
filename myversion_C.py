import pytest


class Token:
	def __init__(self, typ, value):
		self.typ = typ
		self.value = value


def get_integer(text):
	result = ''
	counter = 0

	while text[counter] in '0123456789':
		result += text[counter]
		if counter == len(text)-1:
			break
		counter += 1

	return Token('INT', int(result))






@pytest.mark.parametrize('text, expected', (
    ('1', ('INT', 1)),
    ('11', ('INT', 11)),
    ('11 ', ('INT', 11)),
    ('11 1', ('INT', 11)),
    ('2345', ('INT', 2345)),
    ))
def test_get_next_token_returns_tokens_from_pos(text, expected):
    token = get_integer(text=text)
    assert token.typ == Token(*expected).typ
    assert token.value == Token(*expected).value


if __name__ == '__main__':
    pass

    pytest.main([
        __file__,
        # '-v',
        '-s'
    ])
import program
import pytest


MIMES = [
    ['', program.EOF, program.EOF],
    ['1', program.INTEGER, eval('1')],
]


@pytest.mark.parametrize('src, toktype, tokvalue', MIMES)
def test__can_find_numbers(src, toktype, tokvalue):
    token, idx = program.find_token(src, 0)
    assert token.toktype == toktype
    assert token.tokvalue == tokvalue
    assert idx == len(src)


if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

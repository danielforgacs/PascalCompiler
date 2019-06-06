import program
import pytest


MIMES = [
    ['', program.EOF, program.EOF],
    ['1', program.INTEGER, eval('1')],
    ['12345', program.INTEGER, eval('12345')],
    ['+', program.PLUS, program.PLUS_SYMBOL],
]
FIND_INTEGERS = [
    ['1', 1],
    ['1s', 1],
    ['12345', 12345],
]
FACTOR = [
    '1',
    '123',
    '123090',
]


@pytest.mark.parametrize('src, toktype, tokvalue', MIMES)
def test__can_find_numbers(src, toktype, tokvalue):
    token, idx = program.find_token(src, 0)
    assert token.toktype == toktype
    assert token.tokvalue == tokvalue
    assert idx == len(src)



@pytest.mark.parametrize('src, exp', FIND_INTEGERS)
def test__find_integer(src, exp):
    num, idx = program.find_integer(src, 0)
    assert num == exp
    assert idx == len(str(exp))



@pytest.mark.parametrize('src', FACTOR)
def test__factor(src):
    result, idx = program.factor(src, 0)
    assert result == eval(src)
    assert idx == len(src)


if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

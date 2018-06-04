import interpreter
import pytest


def test_get_next_token_returns_token_01():
    result = interpreter.Interpreter(text='1').get_next_token()
    assert isinstance(result, interpreter.Token)


def test_get_next_token_returns_token_02():
    code = interpreter.Interpreter(text='1+4')
    token1 = code.get_next_token()
    assert token1.value == 1
    assert token1.type_ == interpreter.INTEGER
    token2 = code.get_next_token()
    assert token2.value == '+'
    assert token2.type_ == interpreter.PLUS
    token3 = code.get_next_token()
    assert token3.value == 4
    assert token3.type_ == interpreter.INTEGER



if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s',
    ])

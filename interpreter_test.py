import interpreter
import pytest


@pytest.mark.parametrize('src, expected', [
    ['3+5', 3+5],
    # ['', None]
])
def test_calculator_01(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected


def test_get_next_token():
    interp = interpreter.Interpreter(text='3+5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.PLUS, '+')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)

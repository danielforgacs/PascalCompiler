import interpreter
import pytest


@pytest.mark.parametrize('src, expected', [
    ['3+5', 3+5],
    ['0+0', 0],
    ['9+9', 18],
])
def test_calculator_can_add_single_digits_without_space(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected


def test_get_next_token():
    interp = interpreter.Interpreter(text='3+5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.PLUS, '+')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)

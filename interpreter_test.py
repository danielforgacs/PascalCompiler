import interpreter
import functionalinterpreter as fi
import pytest


@pytest.mark.parametrize('src, expected', [
    ['3+5', 3+5],
    ['0+0', 0],
    ['9+9', 18],
])
def test_calculator_can_add_single_digits_without_space(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected


@pytest.mark.parametrize('src, expected', [
    ['3-5', 3-5],
    ['0-0', 0],
    ['9-9', 9-9],
    ['5-3', 5-3],
])
def test_calculator_can_subtract_single_digits_without_space(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected
    result = fi.exp(src)
    assert result == expected


def test_get_next_token_add():
    interp = interpreter.Interpreter(text='3+5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.PLUS, '+')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)

    token, idx = fi.get_next_token('3+5', 0)
    assert token == fi.Token(fi.INTEGER, 3)
    assert idx == 1
    token, idx = fi.get_next_token('3+5', idx)
    assert token == fi.Token(fi.PLUS, '+')
    assert idx == 2
    token, idx = fi.get_next_token('3+5', idx)
    assert token == fi.Token(fi.INTEGER, 5)
    assert idx == 3


def test_get_next_token_subtract():
    interp = interpreter.Interpreter(text='3-5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.MINUS, '-')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)

    token, idx = fi.get_next_token('3-5', 0)
    assert token == fi.Token(fi.INTEGER, 3)
    assert idx == 1
    token, idx = fi.get_next_token('3-5', idx)
    assert token == fi.Token(fi.MINUS, '-')
    assert idx == 2
    token, idx = fi.get_next_token('3-5', idx)
    assert token == fi.Token(fi.INTEGER, 5)
    assert idx == 3


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', [
    ['31+5', 31+5],
    ['12+0', 12],
    ['5+32', 5+32],
    ['12345+54321', 12345+54321],
])
def test_calculator_can_add_adny_digits_without_space(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected
    result = fi.exp(src)
    assert result == expected


def test_emtpy_string_does_not_crash():
    assert not interpreter.Interpreter('').exp()
    assert not fi.exp('')




@pytest.mark.parametrize('src, expected', [
    ['   31+5', 31+5],
    ['   31   +5', 31+5],
    ['   31   +   5', 31+5],
    ['   31   +   5   ', 31+5],
    ['   31-5', 31-5],
    ['   31   -5', 31-5],
    ['   31   -   5', 31-5],
    ['   31   -   5   ', 31-5],
])
def test_space_is_ok(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected
    result = fi.exp(src)
    assert result == expected




@pytest.mark.parametrize('src, expected', [
    ['0*0', 0*0],
    ['1*0', 1*0],
    ['0*1', 0*1],
    ['1*1', 1*1],
    ['123*321', 123*321],
    ['   31*5', 31*5],
    ['   31   *5', 31*5],
    ['   31   *   5', 31*5],
    ['   31   *   5   ', 31*5],
])
def test_multiply(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected
    result = fi.exp(src)
    assert result == expected



@pytest.mark.parametrize('src, expected', [
    ['0/1', 0/1],
    ['1/1', 1/1],
    ['123/321', 123/321],
    ['   31/5', 31/5],
    ['   31   /5', 31/5],
    ['   31   /   5', 31/5],
    ['   31   /   5   ', 31/5],
])
def test_div(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected
    result = fi.exp(src)
    assert result == expected

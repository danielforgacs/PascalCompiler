import interpreter
import functionalinterpreter as fi
import pytest


cases_01 = [
    ['3+5', 3+5],
    ['0+0', 0],
    ['9+9', 18],
]

@pytest.mark.parametrize('src, expected', cases_01)
def test_calculator_can_add_single_digits_without_space(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


@pytest.mark.parametrize('src, expected', cases_01)
def test_calculator_can_add_single_digits_without_space__func(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected



cases_02 = [
    ['3-5', 3-5],
    ['0-0', 0],
    ['9-9', 9-9],
    ['5-3', 5-3],
]

@pytest.mark.parametrize('src, expected', cases_02)
def test_calculator_can_subtract_single_digits_without_space(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_02)
def test_calculator_can_subtract_single_digits_without_space__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected



# @pytest.mark.skip('')
def test_get_next_token_add():
    interp = interpreter.Lexer(text='3+5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.PLUS, '+')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)



# @pytest.mark.skip('')
def test_get_next_token_add__func():
    token, idx = fi.get_next_token('3+5', 0)
    assert token == fi.Token(fi.INTEGER, 3)
    assert idx == 1
    token, idx = fi.get_next_token('3+5', idx)
    assert token == fi.Token(fi.PLUS, '+')
    assert idx == 2
    token, idx = fi.get_next_token('3+5', idx)
    assert token == fi.Token(fi.INTEGER, 5)
    assert idx == 3



# @pytest.mark.skip('')
def test_get_next_token_subtract():
    interp = interpreter.Lexer(text='3-5')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 3)
    assert interp.get_next_token() == interpreter.Token(interpreter.MINUS, '-')
    assert interp.get_next_token() == interpreter.Token(interpreter.INTEGER, 5)
    assert interp.get_next_token() == interpreter.Token(interpreter.EOF, None)


# @pytest.mark.skip('')
def test_get_next_token_subtract__func():
    token, idx = fi.get_next_token('3-5', 0)
    assert token == fi.Token(fi.INTEGER, 3)
    assert idx == 1
    token, idx = fi.get_next_token('3-5', idx)
    assert token == fi.Token(fi.MINUS, '-')
    assert idx == 2
    token, idx = fi.get_next_token('3-5', idx)
    assert token == fi.Token(fi.INTEGER, 5)
    assert idx == 3



cases_03 = [
    ['31+5', 31+5],
    ['12+0', 12],
    ['5+32', 5+32],
    ['12345+54321', 12345+54321],
]

# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_03)
def test_calculator_can_add_adny_digits_without_space(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_03)
def test_calculator_can_add_adny_digits_without_space__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected



# @pytest.mark.skip('')
def test_emtpy_string_does_not_crash():
    assert not interpreter.Interpreter(interpreter.Lexer('')).expr()



# @pytest.mark.skip('')
def test_emtpy_string_does_not_crash__func():
    assert not fi.expr('')


cases_04 = [
    ['   31+5', 31+5],
    ['   31   +5', 31+5],
    ['   31   +   5', 31+5],
    ['   31   +   5   ', 31+5],
    ['   31-5', 31-5],
    ['   31   -5', 31-5],
    ['   31   -   5', 31-5],
    ['   31   -   5   ', 31-5],
]

# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_04)
def test_space_is_ok(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_04)
def test_space_is_ok__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected



cases_05 = [
    ['0*0', 0*0],
    ['1*0', 1*0],
    ['0*1', 0*1],
    ['1*1', 1*1],
    ['123*321', 123*321],
    ['   31*5', 31*5],
    ['   31   *5', 31*5],
    ['   31   *   5', 31*5],
    ['   31   *   5   ', 31*5],
]

# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_05)
def test_multiply(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected



# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_05)
def test_multiply__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected



cases_06 = [
    ['0/1', 0/1],
    ['1/1', 1/1],
    ['123/321', 123/321],
    ['   31/5', 31/5],
    ['   31   /5', 31/5],
    ['   31   /   5', 31/5],
    ['   31   /   5   ', 31/5],
]

# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_06)
def test_div(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_06)
def test_div__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected




cases_07 = [
    ['1+2+3', 1+2+3],
    ['1+2+3+2+1', 1+2+3+2+1],
    ['12+23+34+25+16', 12+23+34+25+16],
    [' 12  +  23  +    34  +25 + 16  ', 12+23+34+25+16],
    [' 1  + 1  -  1  /  1 * 1 +  1 + 1 - 1  ', 1+1-1/1*1+1+1-1],
]

# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_07)
def test_multiple_op_01(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_07)
def test_multiple_op_01__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected



cases_08 = [
    ['(1)', 1],
    ['((1))', 1],
    ['(((1)))', 1],
    ['(((1+1)))', 1+1],
    ['(1+1)', (1+1)],
    ['(1+1)+1', (1+1)+1],
    [' ( 1 + 1  )  +   1', (1+1)+1],
    ['(1*1)+1', (1*1)+1],
    ['(1*1)/1', (1*1)/1],
    ['(1*(2+3))/1+(4+(5*6))', (1*(2+3))/1+(4+(5*6))],
]

# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_08)
def test_parentheses(src, expected):
    result = interpreter.Interpreter(interpreter.Lexer(src)).expr()
    assert result == expected


# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_08)
def test_parentheses__func(src, expected):
    result = fi.expr(src)[0]
    assert result == expected

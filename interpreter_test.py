import interpreter
import pytest
import sys


PYTHON_VERIONS_MAJOR = (3,)
PYTHON_VERIONS_MINOR = (5, 6)


def test_python_version_ok():
    assert sys.version_info.major in PYTHON_VERIONS_MAJOR
    assert sys.version_info.minor in PYTHON_VERIONS_MINOR


def test_get_next_token_returns_token_01():
    token = interpreter.Lexer(text='1').get_next_token()
    assert isinstance(token, interpreter.Token)


@pytest.mark.skip('CAN`T ADD YET')
def test_get_next_token_returns_token_02():
    code = interpreter.Lexer(text='1+4')
    token1 = code.get_next_token()
    assert token1.value == 1
    assert token1.type == interpreter.INTEGER
    token2 = code.get_next_token()
    assert token2.value == '+'
    assert token2.type == interpreter.PLUS
    token3 = code.get_next_token()
    assert token3.value == 4
    assert token3.type == interpreter.INTEGER


@pytest.mark.skip('CAN`T ADD YET')
def test_eat():
    lexer = interpreter.Lexer(text='1+4')
    interpr = interpreter.Interpreter(lexer=lexer)
    interpr.currenttoken = interpr.lexer.get_next_token()
    assert code.currenttoken.value == 1
    assert code.currenttoken.type_ == interpreter.INTEGER
    code.eat(tokentype=interpreter.INTEGER)
    assert code.currenttoken.value == '+'
    assert code.currenttoken.type_ == interpreter.PLUS
    code.eat(tokentype=interpreter.PLUS)
    assert code.currenttoken.value == 4
    assert code.currenttoken.type_ == interpreter.INTEGER
    code.eat(tokentype=interpreter.INTEGER)


@pytest.mark.skip('CAN`T ADD YET')
def test_expr():
    lexer = interpreter.Lexer(text='1+4')
    code = interpreter.Interpreter(lexer=lexer)
    result = code.expr()
    assert result == 5


@pytest.mark.skip('CAN`T ADD YET')
@pytest.mark.parametrize('codetext, expected', (
    ('0+0', 0),
    ('1+2', 3),
    ('8+7', 15),
    ))
def test_can_add_single_digit_no_space(codetext, expected):
    program = interpreter.Interpreter(text=codetext)
    result = program.expr()
    assert result == expected


@pytest.mark.skip('CAN`T ADD YET')
@pytest.mark.parametrize('codetext, expected', (
    ('0-0', 0),
    ('9-4', 5),
    ('1-2', -1),
    ('8-7', 1),
    ))
def test_can_subtract_single_digit_no_space(codetext, expected):
    program = interpreter.Interpreter(text=codetext)
    result = program.expr()
    assert result == expected


@pytest.mark.skip('CAN`T ADD YET')
@pytest.mark.parametrize('codetext, expected', (
    ('0 - 0', 0),
    ('9  - 4', 5),
    ('1-    2', -1),
    ('   8-7    ', 1),
    ))
def test_can_subtract_single_digit_with_space(codetext, expected):
    program = interpreter.Interpreter(text=codetext)
    result = program.expr()
    assert result == expected


@pytest.mark.skip('CAN`T ADD YET')
@pytest.mark.parametrize('codetext, expected', (
    ('20 - 20', 0),
    ('200 - 200', 0),
    ('1000   +    200', 1200),
    ('1000   -    200', 800),
    ('0   -    200', -200),
    ('1   -    200', -199),
    ))
def test_multidigit_works(codetext, expected):
    program = interpreter.Interpreter(text=codetext)
    result = program.expr()
    assert result == expected


# @pytest.mark.skip()
@pytest.mark.parametrize('codetext, expected', (
    ('1*1', 1),
    ('2*2', 2*2),
    ('0*2', 0*2),
    ('123*456', 123*456),
    ('123  *   456', 123*456),
    ))
def test_can_multiply(codetext, expected):
    lexer = interpreter.Lexer(text=codetext)
    program = interpreter.Interpreter(lexer=lexer)
    result = program.expr()
    assert result == expected


# @pytest.mark.skip()
@pytest.mark.parametrize('codetext, expected', (
    ('1/1', 1/1),
    ('1  /  1', 1/1),
    ('10  /  1', 10/1),
    ('1  /  10', 1/10),
    ('66  /  22', 66/22),
    ))
def test_can_divide(codetext, expected):
    lexer = interpreter.Lexer(text=codetext)
    program = interpreter.Interpreter(lexer=lexer)
    result = program.expr()
    assert result == expected


@pytest.mark.skip('CAN`T ADD YET')
@pytest.mark.parametrize('codetext, expected', (
    ('1-1-1', 1-1-1),
    ('1-1-1-1-1-1', 1-1-1-1-1-1),
    ('1-1+1-1+1-1+1-1+1-1', 1-1+1-1+1-1+1-1+1-1),
    ('1  - 1 +1- 1+1-1  +1-1+1-1', 1-1   +1-  1+1-   1+1-1+1-1),
    ('123  -1987+   14- 156-0   +1', 123  -1987+   14- 156-0   +1),
    ))
def test_can_repeat_add_sub(codetext, expected):
    lexer = interpreter.Lexer(text=codetext)
    program = interpreter.Interpreter(lexer=lexer)
    result = program.expr()
    assert result == expected


@pytest.mark.parametrize('codetext, expected', (
    ('2*2*2', 2*2*2),
    ('2*2*2*2*2*2', 2*2*2*2*2*2),
    ('2/2/2', 2/2/2),
    ('2/2/2/2/2/2', 2/2/2/2/2/2),
    ('3*3/3*3/3*3/3*3/3*3', 3*3/3*3/3*3/3*3/3*3),
    ('3  / 3 *3/ 3*3/3  *3/3*3/3', 3/3   *3/  3*3/   3*3/3*3/3),
    ('123  /1987*   14/ 156/10   *1', 123  /1987*   14/ 156/10   *1),
    ))
def test_can_repeat_add_sub_mult_div_spaced(codetext, expected):
    lexer = interpreter.Lexer(text=codetext)
    program = interpreter.Interpreter(lexer=lexer)
    result = program.expr()
    assert result == expected


if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s',
    ])

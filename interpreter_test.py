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


def test_eat():
    code = interpreter.Interpreter(text='1+4')
    code.currenttoken = code.get_next_token()
    assert code.currenttoken.value == 1
    assert code.currenttoken.type_ == interpreter.INTEGER
    code.eat(tokentype=interpreter.INTEGER)
    assert code.currenttoken.value == '+'
    assert code.currenttoken.type_ == interpreter.PLUS
    code.eat(tokentype=interpreter.PLUS)
    assert code.currenttoken.value == 4
    assert code.currenttoken.type_ == interpreter.INTEGER
    code.eat(tokentype=interpreter.INTEGER)


def test_expr():
    code = interpreter.Interpreter(text='1+4')
    result = code.expr()
    assert result == 5

if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s',
    ])

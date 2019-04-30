import interpreter
import pytest


@pytest.mark.parametrize('src, expected', [
    ['3+5', 3+5],
])
def test_calculator_01(src, expected):
    result = interpreter.Interpreter(src).exp()
    assert result == expected

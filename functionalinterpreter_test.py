import functionalinterpreter as fi
import pytest



@pytest.mark.parametrize('src, exp', [
    [['1', 0], (1, 1)],
    [['1 ', 0], (1, 1)],
    [['1b', 0], (1, 1)],
    [['1111', 0], (1111, 4)],
    [['1111bbb', 0], (1111, 4)],
    [['1111   ', 0], (1111, 4)],
    [['00001111   ', 0], (1111, 8)],
    [['0000111100   ', 0], (111100, 10)],
    [['0000987600   ', 0], (987600, 10)],
    ])
def test_integer(src, exp):
    result = fi.integer(*src)
    assert result == exp

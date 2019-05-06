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




@pytest.mark.parametrize('src, exp', [
    [[' ', 0], (' ', 1)],
    [['  ', 0], ('  ', 2)],
    [['  1', 0], ('  1', 2)],
    [['1   ', 0], ('1   ', 0)],
    [['1   ', 1], ('1   ', 4)],
    [['1   567', 1], ('1   567', 4)],
    [['1   567 ', 6], ('1   567 ', 6)],
    [['1   567 ', 7], ('1   567 ', 8)],
    ])
def test_skip_whitespace(src, exp):
    result = fi.skip_whitespace(*src)
    assert result == exp

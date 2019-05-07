import pytest
import functionalinterpreter as fi



# @pytest.mark.skip('')
def test_expr_finds_EOF():
    result = fi.expr('')
    assert result == (None, 0)


def test_get_token_find_EOF():
    assert fi.find_token('', 0)[0] == fi.Token(fi.EOF, fi.EOF)


cases_01 = [
    [['1', 0], (fi.Token(fi.INTEGER, 1), 1)],
    [['12', 0], (fi.Token(fi.INTEGER, 12), 2)],
    [[' 12', 1], (fi.Token(fi.INTEGER, 12), 3)],
]
# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_01)
def test_get_token(src, expected):
    assert fi.find_token(*src) == expected


cases_02 = [
    [['1', 0], (1, 1)],
    [['12', 0], (12, 2)],
    [['12 ', 0], (12, 2)],
    [[' 12 ', 1], (12, 3)],
    [[' 02 ', 1], (2, 3)],
]
# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_02)
def test_find_integer(src, expected):
    assert fi.find_integer(*src) == expected


cases_03 = [
    [['1', 0], (1, 1)],
    [['12', 0], (12, 2)],
    [[' 12', 1], (12, 3)],
    [['  123  ', 2], (123, 5)],
]
@pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_03)
def test_expr_01(src, expected):
    assert fi.expr(*src) == expected


cases_04 = [
    [[' ', 0], (' ', 1)],
    [[' ', 1], (' ', 1)],
    [['  ', 1], ('  ', 2)],
    [['  1', 1], ('  1', 2)],
]
@pytest.mark.parametrize('src, expected', cases_04)
def test_skip_whitespace(src, expected):
    assert fi.skip_whitespace(*src) == expected



cases_05 = [
    [['1'], (1, 1)],
    [[' 1'], (1, 2)],
    [[' 12'], (12, 3)],
    [[' 12 3', 4], (3, 5)],
    [[' 12 3 ', 4], (3, 5)],
    [[' 12 3 444', 4], (3, 5)],
]
@pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_05)
def test_expr_ignores_whitespace(src, expected):
    assert fi.expr(*src) == expected


cases_06 = [
    [['+', 0], (fi.Token(fi.PLUS, '+'), 1)],
    [[' +', 0], (fi.Token(fi.PLUS, '+'), 2)],
    [['  +', 0], (fi.Token(fi.PLUS, '+'), 3)],
    [['  +', 1], (fi.Token(fi.PLUS, '+'), 3)],
    [['  + ', 1], (fi.Token(fi.PLUS, '+'), 3)],
]
# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_06)
def test_find_token_finds_PLUS(src, expected):
    assert fi.find_token(*src) == expected



cases_07 = [
    [['1+1'], (1+1, 3)],
    [['11+1'], (11+1, 4)],
    [['11 + 1'], (11+1, 6)],
    [['  11 + 1'], (11+1, 8)],
    [['  11 + 1  +2'], (11+1+2, 12)],
]
# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', cases_07)
def test_expr_addition(src, expected):
    assert fi.expr(*src) == expected



if __name__ == '__main__':
    pytest.main([
        __file__,
        # '-s',
    ])

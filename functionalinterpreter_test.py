import pytest
import functionalinterpreter as fi



@pytest.mark.skip('')
def test_expr_finds_EOF():
    result = fi.expr('')
    assert result == None


def test_get_token_find_EOF():
    assert fi.find_token('', 0)[0] == fi.Token(fi.EOF, fi.EOF)


cases_01 = [
    [['1', 0], (fi.Token(fi.INTEGER, 1), 1)],
    # [['12', 0], (fi.Token(fi.INTEGER, 12), 2)],
]
@pytest.mark.parametrize('src, expected', cases_01)
def test_get_token(src, expected):
    assert fi.find_token(*src) == expected




if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s',
    ])

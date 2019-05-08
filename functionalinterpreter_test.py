import pytest
import functionalinterpreter as fi


FIND_INTEGERS = [
    ['1', 0, (1, 1)],
    ['123', 0, (123, 3)],
    ['  123', 2, (123, 5)],
    ['  123 ', 2, (123, 5)],
    ['  123s ', 2, (123, 5)],
    ['  123 45 s ', 2, (123, 5)],
    ['  123 45 s ', 6, (45, 8)],
]

EXPR = [
    ['1', (1, 1)],
    ['12', (12, 2)],
    ['12345', (12345, 5)],
]




def test_find_token_tokenizes_source():
    src = ('123 456   98765 ++1 003+')
    idxs = [3, 7, 15, 17, 18, 19, 23, 24]
    values = iter([123, 456, 98765, '+', '+', 1, 3, '+', 'EOF'])
    tokentypes = iter([
        fi.INTEGER,
        fi.INTEGER,
        fi.INTEGER,
        fi.PLUS,
        fi.PLUS,
        fi.INTEGER,
        fi.INTEGER,
        fi.PLUS,
        fi.EOF,
    ])

    result = fi.find_token(src, 0)

    for idx in idxs:
        assert result == (fi.Token(next(tokentypes), next(values)), idx)
        result = fi.find_token(src, idx)

    assert result == (fi.Token(fi.EOF, fi.EOF), idxs[-1])




@pytest.mark.parametrize('src, idx, expected', FIND_INTEGERS)
def test_find_integer_finds_integers(src, idx, expected):
    assert fi.find_integer(src, idx) == expected




@pytest.mark.parametrize('src, expected', EXPR)
def test_expr(src, expected):
    assert fi.expr(src, 0) == expected




if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])

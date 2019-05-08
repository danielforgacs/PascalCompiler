import pytest
import functionalinterpreter as fi



def test_find_token_tokenizes_source():
    src = '123 456   98765 ++'
    idxs = [3, 7, 15, 17, 18, 18]
    values = iter([123, 456, 98765, '+', '+', 'EOF'])
    tokentypes = iter([
        fi.INTEGER,
        fi.INTEGER,
        fi.INTEGER,
        fi.PLUS,
        fi.PLUS,
        fi.EOF,
    ])

    result = fi.find_token(src, 0)

    for idx in idxs:
        assert result == (fi.Token(next(tokentypes), next(values)), result[1])
        result = fi.find_token(src, idx)

    assert result == (fi.Token(fi.EOF, fi.EOF), result[1])



if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])

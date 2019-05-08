import pytest
import functionalinterpreter as fi



def test_find_token_tokenizes_source():
    src = '123 456   98765 +'
    idxs = iter([3, 7, 15, 17, 17])
    values = iter([123, 456, 98765, '+', 'EOF'])
    tokentypes = iter([
        fi.INTEGER,
        fi.INTEGER,
        fi.INTEGER,
        fi.PLUS,
        fi.EOF,
    ])

    result = fi.find_token(src, 0)
    assert result == (fi.Token(next(tokentypes), next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(next(tokentypes), next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(next(tokentypes), next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(next(tokentypes), next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(next(tokentypes), next(values)), next(idxs))




if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])

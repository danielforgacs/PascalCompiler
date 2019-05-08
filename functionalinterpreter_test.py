import pytest
import functionalinterpreter as fi



def test_find_token_tokenizes_source():
    src = '123 456   98765'
    idxs = iter([3, 7, 15])
    values = iter([123, 456, 98765])

    result = fi.find_token(src, 0)
    assert result == (fi.Token(fi.INTEGER, next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(fi.INTEGER, next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(fi.INTEGER, next(values)), next(idxs))
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(fi.EOF, fi.EOF), len(src))




if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s'
    ])

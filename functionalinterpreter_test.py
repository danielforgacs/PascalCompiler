import pytest
import functionalinterpreter as fi



def test_find_token_tokenizes_source():
    src = '123'

    result = fi.find_token(src, 0)
    assert result == (fi.Token(fi.INTEGER, 1), 3)
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(fi.EOF, fi.EOF), len(src))




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

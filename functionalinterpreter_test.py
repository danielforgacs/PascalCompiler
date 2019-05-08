import pytest
import functionalinterpreter as fi



def test_find_token_tokenizes_source():
    src = '1'

    result = fi.find_token(src, 0)
    assert result == (fi.Token(fi.INTEGER, 1), 1)
    result = fi.find_token(src, result[1])
    assert result == (fi.Token(fi.EOF, fi.EOF), 2)




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

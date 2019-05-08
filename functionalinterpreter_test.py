import pytest
import functionalinterpreter as fi



def test_find_token_tokenizes_source():
    src = ''

    result = fi.find_token(src, 0)
    assert result == (fi.Token(fi.EOF, fi.EOF), 1)




if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

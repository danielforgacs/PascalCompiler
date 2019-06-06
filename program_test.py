import program
import pytest


MIMES = [
    ['', program.EOF, program.EOF],
]


@pytest.mark.parametrize('src, toktype, tokvalue', MIMES)
def test__can_find_numbers(src, toktype, tokvalue):
    result = program.find_token(src, 0)
    assert result.toktype == toktype
    assert result.tokvalue == tokvalue


if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

import program
import pytest


MIMES = [
    ['', program.Token(program.EOF, program.EOF)],
]


@pytest.mark.parametrize('src', MIMES)
def test__can_find_numbers(src):
    program.find_token(src, 0)


if __name__ == '__main__':
    pytest.main([
        __file__,
    ])

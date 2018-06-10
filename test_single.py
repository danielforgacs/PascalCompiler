import interpreter
import pytest
import sys


PYTHON_VERIONS_MAJOR = (3,)
PYTHON_VERIONS_MINOR = (5,)


def test_python_version_ok():
    assert sys.version_info.major in PYTHON_VERIONS_MAJOR
    assert sys.version_info.minor in PYTHON_VERIONS_MINOR


@pytest.mark.parametrize('codetext, expected', (
    ('5', 5),

    ('2*3', 2*3),
    ('2/3', 2/3),

    ('2  *  3', 2*3),
    ('2  /    3', 2/3),

    ('2  *  3  * 4', 2*3*4),
    ('2  /    3   / 2', 2/3/2),

    ('2*4/8*16/32*64', 2*4/8*16/32*64),
    ('2*  4  /8  *16  /32 * 64', 2*4/8*16/32*64),
    ))
def test_can_add_single_digit_no_space(codetext, expected):
    lexer = interpreter.Lexer(text=codetext)
    program = interpreter.Interpreter(lexer=lexer)
    result = program.expr()
    assert result == expected




if __name__ == '__main__':
    pytest.main([
        __file__,
        '-s',
    ])

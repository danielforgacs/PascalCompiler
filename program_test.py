import program
import pytest


MIMES = [
    ['', program.EOF, program.EOF],
    ['1', program.INTEGER, eval('1')],
    ['12345', program.INTEGER, eval('12345')],
    ['+', program.PLUS, program.PLUS_SYMBOL],
    ['(', program.L_PAREN, program.L_PAREN_SYMBOL],
    [')', program.R_PAREN, program.R_PAREN_SYMBOL],
    [';', program.SEMI, program.SEMI_SYMBOL]
]
FIND_INTEGERS = [
    ['1', 1],
    ['1s', 1],
    ['12345', 12345],
]
FACTOR = [
    ['1', 1],
    ['123', 123],
    ['123090', 123090],
    ['(123090)', 123090],
    ['((123090))', 123090],
    ['(((123090))', 123090],
    ['(((((((123090))))))', 123090],
]
NODE_VISITOR = [
    '1',
    '12345',
    '(12345)',
    '((12345))',
    '(((((((((12345)))))))))',
]
PROGRAM = [
    ['1', [1]],
    ['((((123))))', [123]],
    ['2+3', [5]],
    ['1;2', [1, 2]],
    ['1;2;3;4;5', [1, 2, 3, 4, 5]],
    ['1+2;2+3;3+4;4+5;5+6', [3, 5, 7, 9, 11]],
    ['12+(21);(22+31);13+14;((((14))))+15;(((53+61)))',
    [12+(21), (22+31), 13+14, ((((14))))+15, (((53+61)))]],
]


@pytest.mark.parametrize('src, type_, value', MIMES)
def test__can_find_numbers(src, type_, value):
    token, idx = program.find_token(src, 0)
    assert token.type_ == type_
    assert token.value == value
    assert idx == len(src)



@pytest.mark.parametrize('src, exp', FIND_INTEGERS)
def test__find_integer(src, exp):
    num, idx = program.find_integer(src, 0)
    assert num == exp
    assert idx == len(str(exp))



@pytest.mark.parametrize('src, expected', FACTOR)
def test__factor(src, expected):
    node, idx = program.factor(src, 0)
    assert node.value == expected
    assert idx == len(src)


@pytest.mark.parametrize('src', NODE_VISITOR)
def test__node_visitor(src):
    node, _ = program.factor(src, 0)
    result = program.node_visitor(node)
    assert result == eval(src)



@pytest.mark.parametrize('src, expected', PROGRAM)
def test__program(src, expected):
    assert program.program(src) == expected


if __name__ == '__main__':
    pytest.main([
        __file__,
        # '-s',
        # '-x',
    ])

import pytest
import functionalinterpreter as fi


FIND_INTEGERS = [
    ['1', 0, (1, 1)],
    ['123', 0, (123, 3)],
    ['  123', 2, (123, 5)],
    ['  123 ', 2, (123, 5)],
    ['  123s ', 2, (123, 5)],
    ['  123 45 s ', 2, (123, 5)],
    ['  123 45 s ', 6, (45, 8)],
]

EXPR = [
    ['1', fi.Num(fi.Token(fi.INTEGER, 1))],
    ['12', fi.Num(fi.Token(fi.INTEGER, 12))],
    ['12345', fi.Num(fi.Token(fi.INTEGER, 12345))],
    # ['1+1', fi.Num(fi.Token(fi.INTEGER, 1+1))],
    # ['1+1', (2, 3)],
    # ['123+456', (123+456, 7)],
    # ['  123   +   456', (123+456, 15)],

    # ['1+1+1', (3, 5)],
    # ['1+1+1+1+1+1+1', (1+1+1+1+1+1+1, 13)],

    # ['1+1-1+1-1+1-1', (1+1-1+1-1+1-1, 13)],
    # ['0-0-0-0', (0, 7)],

    # ['123+321-234', (123+321-234, 11)],

    # ['11+111+11+11', (11+111+11+11, 12)],
    # ['11+112-11+0', (11+112-11+0, 11)],
    # ['11+112-11+000', (11+112-11+000, 13)],

    # ['00+01-00+00', (1, 11)],
    # ['00+01-01+00', (0, 11)],

    # ['2+2-2+2', (2+2-2+2, 7)],

    # ['11+112-11+001', (11+112-11+1, 13)],
    # ['11+11-11+11', (11+11-11+11, 11)],
    # ['123+321-234+432', (123+321-234+432, 15)],

    # ['  123 +  321 - 234  +   432', (123+321-234+432, 27)],
]

PAREN = [
    ['(1)', 1],
    ['((1))', 1],
    ['(1+1)', 2],
    [' ( 1  +1  )', 2],
    ['(1+1)+1', 3],
    ['(10+10)+10', 30],
    [' (  111  +222  )   +334', (111+222)+334],
    [' (  111  +222  )   +(334)', (111+222)+334],
    [' (  111  +222  )   +(334)', (111+222)+334],
    [' (  111  +222  )   +(334) - (4 + 2)', (111+222)+(334)-(4+2)],
    ['1+(2+(3+(4+(5+(6+(7)+8)+9)+10)))', 1+(2+(3+(4+(5+(6+(7)+8)+9)+10)))]
]

TERM = [
    '1*1',
    '10*2',
    '   10*2',
    '   10  *   2',
    '   10  *   223',
    '   10  *   223 * 2',
    '2*4/2*8/4',
    '2  * 4  / 2  * 8 /   4',
    '22  * 42  / 2  * 800 /   40',
    '100000   / 1000'
    '100000   / 1000 * 12480   / 200'
]

EXPR_TERM = [
    '1*2',
    '(1*2)',
    '(1*2)*3',
    '((((1*2)*3)))',
    '((((1*2)*3)+2)/1)',
    '((((12*21)*33)+22)/10)',
    '((((  12 * 21) * 33) + 22 ) / 10)',
    '( ((  (  12 * 21) * 33) + 22 ) / 10   )',
]

EPR_PLUS_MINUS_MULT_DIV_PAREN = [
    '(1)+(2)',
    '(12)+(21)',
    '(12)+(21)*(24)/(2)',
    '((12)+(21))*(24)/(2)',
    '((12)+(21))*((24)/(2))',
    '(((12)+(21))*((24)/(2)))+((((12)+(21))*((24)/(2))))*(((12)+(21))*((24)/(2)))',
    (' ( ( ( 12) + ( 21) ) * ( (24) /  ( 2))) +  (((   (12)+(21))'
        ' *( ( 24) / (2  ) )) ) * ( (( 12) + ( 21) )*((24)/ (2  ) )  )'),
    (' ( ( ( 12+  23+36) + ( 21) ) * ( (24) /  ( 2))) +  (((   (12)+(21))'
        ' *( ( 24*3+2*3) / (2  ) )) ) * ( (( 12) + ( 21) )*((24)/ (2  ) )  )'),
]



INTERPRETER = [
    '1+1',
    '+1',
    '-1',
    '++1',
    '--1',
    '++++++1',
    '------1',
    '+-+-+-1',
    '-+-+-+1',
    '(+(-+(-+(-(1)))))',
    '(-(+-(+-(+(1)))))',
    ' ( -( + -( +- (  +(   1 ) )  ) ) )',
    ' ( -( + -( +- (  +(   1 ) )  ) ) ) + (3) * (2)',
]




def test_find_token_tokenizes_source():
    src = '123'
    idxs = [len(src)]
    values_items = [123]
    tokentypes_items = [fi.INTEGER]

    src += ' 456'
    idxs += [len(src)]
    values_items += [456]
    tokentypes_items += [fi.INTEGER]

    src += '   98765'
    idxs += [len(src)]
    values_items += [98765]
    tokentypes_items += [fi.INTEGER]

    src += ' +'
    idxs += [len(src)]
    values_items += ['+']
    tokentypes_items += [fi.PLUS]

    src += '+'
    idxs += [len(src)]
    values_items += ['+']
    tokentypes_items += [fi.PLUS]

    src += '1'
    idxs += [len(src)]
    values_items += [1]
    tokentypes_items += [fi.INTEGER]

    src += ' 003'
    idxs += [len(src)]
    values_items += [3]
    tokentypes_items += [fi.INTEGER]

    src += '+'
    idxs += [len(src)]
    values_items += ['+']
    tokentypes_items += [fi.PLUS]

    src += '-'
    idxs += [len(src)]
    values_items += ['-']
    tokentypes_items += [fi.MINUS]

    src += '  -'
    idxs += [len(src)]
    values_items += ['-']
    tokentypes_items += [fi.MINUS]

    src += '    variablename'
    idxs += [len(src)]
    values_items += ['variablename']
    tokentypes_items += [fi.IDENTIFIER]

    src += ' -'
    idxs += [len(src)]
    values_items += ['-']
    tokentypes_items += [fi.MINUS]

    src += '-'
    idxs += [len(src)]
    values_items += ['-']
    tokentypes_items += [fi.MINUS]

    src += '('
    idxs += [len(src)]
    values_items += ['(']
    tokentypes_items += [fi.PAREN_LEFT]

    src += ' )'
    idxs += [len(src)]
    values_items += [')']
    tokentypes_items += [fi.PAREN_RIGHT]

    src += ' 1'
    idxs += [len(src)]
    values_items += [1]
    tokentypes_items += [fi.INTEGER]

    src += ')'
    idxs += [len(src)]
    values_items += [')']
    tokentypes_items += [fi.PAREN_RIGHT]

    src += ')'
    idxs += [len(src)]
    values_items += [')']
    tokentypes_items += [fi.PAREN_RIGHT]

    src += '   BEGIN'
    idxs += [len(src)]
    values_items += ['BEGIN']
    tokentypes_items += [fi.BEGIN]

    src += '   BEGIN'
    idxs += [len(src)]
    values_items += [fi.BEGIN]
    tokentypes_items += [fi.BEGIN]

    src += '    variablename'
    idxs += [len(src)]
    values_items += ['variablename']
    tokentypes_items += [fi.IDENTIFIER]

    src += '*'
    idxs += [len(src)]
    values_items += ['*']
    tokentypes_items += [fi.MULT]

    src += '/'
    idxs += [len(src)]
    values_items += ['/']
    tokentypes_items += [fi.DIV]

    src += ' ;'
    idxs += [len(src)]
    values_items += [';']
    tokentypes_items += [fi.SEMICOLON]

    src += '   98765'
    idxs += [len(src)]
    values_items += [98765]
    tokentypes_items += [fi.INTEGER]

    src += '    END'
    idxs += [len(src)]
    values_items += ['END']
    tokentypes_items += [fi.END]

    src += ' +'
    idxs += [len(src)]
    values_items += ['+']
    tokentypes_items += [fi.PLUS]

    src += ' .'
    idxs += [len(src)]
    values_items += ['.']
    tokentypes_items += [fi.DOT]

    src += '    END'
    idxs += [len(src)]
    values_items += [fi.END]
    tokentypes_items += [fi.END]

    src += '+'
    idxs += [len(src)]
    values_items += ['+']
    tokentypes_items += [fi.PLUS]

    src += '    END'
    idxs += [len(src)]
    values_items += ['END']
    tokentypes_items += [fi.END]

    src += '    *'
    idxs += [len(src)]
    values_items += ['*']
    tokentypes_items += [fi.MULT]

    src += '    *'
    idxs += [len(src)]
    values_items += ['*']
    tokentypes_items += [fi.MULT]

    values = iter(values_items)
    tokentypes = iter(tokentypes_items)

    result = fi.find_token(src, 0)

    for idx in idxs:
        assert result == (fi.Token(next(tokentypes), next(values)), idx)
        result = fi.find_token(src, idx)

    assert result == (fi.Token(fi.EOF, fi.EOF_SYMBOL), idxs[-1]+1)




@pytest.mark.parametrize('src, idx, expected', FIND_INTEGERS)
def test_find_integer_finds_integers(src, idx, expected):
    assert fi.find_integer(src, idx) == expected




# @pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', EXPR)
def test_expr(src, expected):
    assert fi.expr(src, 0) == (expected, len(src))




@pytest.mark.skip('')
@pytest.mark.parametrize('src, expected', PAREN)
def test_expr_parenthesis(src, expected):
    assert fi.expr(src, 0) == (expected, len(src))




@pytest.mark.skip('')
@pytest.mark.parametrize('src', TERM)
def test_term(src):
    assert fi.term(src, 0) == (eval(src), len(src))




@pytest.mark.skip('')
@pytest.mark.parametrize('src', EXPR_TERM)
def test_expr_term(src):
    assert fi.term(src, 0) == (eval(src), len(src))




@pytest.mark.skip('')
@pytest.mark.parametrize('src', EPR_PLUS_MINUS_MULT_DIV_PAREN)
def test_expr_epr_plus_minus_mult_div_paren(src):
    assert fi.expr(src, 0) == (eval(src), len(src))



@pytest.mark.parametrize('src', INTERPRETER)
def test_expr_epr_plus_minus_mult_div_paren(src):
    assert fi.interpreter(src) == eval(src)




if __name__ == '__main__':
    pytest.main([
        __file__+'::test_find_token_tokenizes_source',
        # '-s'
    ])

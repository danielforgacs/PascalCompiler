import os
import pytest

sys = os.sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import source.interpreter as itpr



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}*{1}'.format(k, i), k*i] for k in range(10) for i in range(10)
])
def test_interpreter_multiplies_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0} + {1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   +     {1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_with_whitespace_2(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0} + {1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   +   {1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_with_whitespace_2(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   *   {1}'.format(k, i), k*i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_multiplies_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



@pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   /   {1}'.format(k, i), k/i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_divides_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()



<<<<<<< HEAD
@pytest.mark.parametrize('expr, result', [
    ['1+1+1', 1+1+1],
    ['1+1+1+1', 1+1+1+1],
    ['1+1+1+1+1+1+1', 1+1+1+1+1+1+1],
])
def test_handles_multiple_integers(expr, result):
    assert itpr.Interpreter(expr).expr() == result



@pytest.mark.parametrize('expr, result', [
    ['1 + 1 + 1 +    1', 1+1+1+1],
    ['2 + 4   +   5 +    9', 2+4+5+9],
])
def test_handles_multiple_integers(expr, result):
    assert itpr.Interpreter(expr).expr() == result



# @pytest.mark.parametrize('expr, result', [
#     ['2 * 3 * 5', 2*3*5],
#     ['2  *   3   *   5', 2*3*5],
#     ['2 *5 +3   *2', 2*5+3*2],
# ])
# def test_01(expr, result):
#     assert itpr.Interpreter(expr).expr() == result
=======
def test_10():
    text = '6*5'
    assert 6*5 == itpr.Interpreter(itpr.Lexer(text)).expr()
>>>>>>> 2c551fe705ee6d0cf362b4ecfc801209d8616d60



if __name__ == '__main__':
    args = [
        os.path.basename(__file__),
        # '-s'
    ]
    pytest.main(args)
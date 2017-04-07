import os
import pytest

sys = os.sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import source.interpreter as itpr



<<<<<<< HEAD
# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}*{1}'.format(k, i), k*i] for k in range(10) for i in range(10)
])
def test_interpreter_multiplies_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0} + {1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   +     {1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_with_whitespace_2(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0} + {1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   +   {1}'.format(k, i), k+i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_adds_multidigit_integers_with_whitespace_2(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   *   {1}'.format(k, i), k*i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_multiplies_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



# @pytest.mark.skip('')
@pytest.mark.parametrize('userinput, result', [
    ['{0}   /   {1}'.format(k, i), k/i] for k in range(90, 100) for i in range(90, 100)
])
def test_interpreter_divides_multidigit_integers_with_whitespace(userinput, result):
    assert result == itpr.Interpreter(itpr.Lexer(userinput)).expr()



def test_10():
    text = '6*5'
    assert 6*5 == itpr.Interpreter(itpr.Lexer(text)).expr()
=======
def test_interpreter_adds_singledigit_integers_no_whitespace():
    assert  1 * 1== itpr.Interpreter(itpr.Lexer('1*1')).expr()
>>>>>>> 9abdae95c8dd8f01931aabeb80dfc12a9c02950f



if __name__ == '__main__':
    args = [
        os.path.basename(__file__),
        # '-s'
    ]
    pytest.main(args)
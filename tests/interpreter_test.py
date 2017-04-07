import os
import pytest

sys = os.sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import source.interpreter as itpr



def test_interpreter_01():
    assert  1 * 1 == itpr.Interpreter(itpr.Lexer('1*1')).expr()

def test_interpreter_02():
    assert  1 * 1 == itpr.Interpreter(itpr.Lexer('1   *    1')).expr()

def test_interpreter_03():
    assert  6 * 8 == itpr.Interpreter(itpr.Lexer('6 * 8')).expr()

def test_interpreter_04():
    assert  6 * 0 == itpr.Interpreter(itpr.Lexer('6 * 0')).expr()



if __name__ == '__main__':
    args = [
        os.path.basename(__file__),
        # '-s'
    ]
    pytest.main(args)
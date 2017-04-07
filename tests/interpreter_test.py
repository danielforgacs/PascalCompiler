import os
import pytest

sys = os.sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import source.interpreter as itpr



def test_interpreter_adds_singledigit_integers_no_whitespace():
    assert  1 * 1== itpr.Interpreter(itpr.Lexer('1*1')).expr()



if __name__ == '__main__':
    args = [
        os.path.basename(__file__),
        # '-s'
    ]
    pytest.main(args)
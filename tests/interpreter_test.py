import os
import pytest

sys = os.sys
sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

import source.interpreter as itpr


@pytest.mark.parametrize('userinput, result', [
    ['{0}+{1}'.format(k, i), k+i] for k in range(10) for i in range(10)
])
def test_interpreter_adds_singledigit_integers_no_whitespace(userinput, result):
    assert result == itpr.Interpreter(userinput).expr()


if __name__ == '__main__':
    args = [
        os.path.basename(__file__),
        # '-s'
    ]
    pytest.main(args)
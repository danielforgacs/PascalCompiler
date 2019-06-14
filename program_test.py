import program
import pytest


SRC_01 = """
BEGIN
    BEGIN
        123;
    END
        234;
        678
END.
"""

TOKENS_01 = [
    program.BEGIN_TOKEN,
    program.BEGIN_TOKEN,
    (program.INTEGER, 123),
    (program.SEMI, program.SEMI_SYMBOL),
    program.END_TOKEN,
    (program.INTEGER, 234),
    (program.SEMI, program.SEMI_SYMBOL),
    (program.INTEGER, 678),
    program.END_TOKEN,
    program.DOT_TOKEN,
]


def test__tokenize_01():
    idx = 0

    for expectedtoken in TOKENS_01:
        token, idx = program.find_token(SRC_01, idx)
        assert token == expectedtoken



def test__program_01():
    src = """
BEGIN
END.
        """
    program.nodevisitor(program.program(src, 0))


def test__program_02():
    src = """
BEGIN
END
BEGIN
END
BEGIN
END
BEGIN
END.
    """
    program.nodevisitor(program.program(src, 0))


def test__program_03():
    src = """
BEGIN
    BEGIN
        BEGIN
            BEGIN
                BEGIN
                    BEGIN
                        BEGIN
                            BEGIN
                            END
                        END
                    END
                END
            END
        END
    END
    BEGIN
        BEGIN
        END
    END
    BEGIN
        BEGIN
            BEGIN
            END
        END
    END
    BEGIN
        BEGIN
        END
    END
END.
    """
    program.nodevisitor(program.program(src, 0))




if __name__ == '__main__':
    pytest.main([
        __file__,
        # '-s',
        # '-x',
    ])

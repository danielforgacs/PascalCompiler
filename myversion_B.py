import pytest


def get_next_token(text, pos):
    token = ''

    while text[pos] in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        token += text[pos]
        pos +=1

        if pos == len(text):
            break

    return token, pos




@pytest.mark.parametrize('text, pos, expected', (
    ('1', 0, '1'),
    ('11', 0, '11'),
    ('11+', 0, '11'),
    ('11    ', 0, '11'),
    ('112345    ', 0, '112345'),
    ))
def test_get_next_token_returns_tokens_from_pos(text, pos, expected):
    token = get_next_token(text=text, pos=pos)
    assert token[0] == expected


if __name__ == '__main__':
    pass

    pytest.main([
        __file__,
        # '-s'
    ])
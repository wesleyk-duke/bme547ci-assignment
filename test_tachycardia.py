import pytest


@pytest.mark.parametrize('test_input,expected',
                         [('tachycardic', True), ('AtachycardicA', True),
                          ('TACHYCARDIC', True), ('TaChYcArDiC', True),
                          ('sponge', False)])
def test_is_tachycardic(test_input, expected):
    from tachycardia import is_tachycardic

    answer = is_tachycardic(test_input)
    assert answer == expected

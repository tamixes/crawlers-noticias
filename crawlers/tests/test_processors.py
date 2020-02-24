import pytest

from crawlers.processors import clean_termos, find_termo


input_find_termo = [
    (r'\w+', 'abc123', 0, 'abc123'),
    (r'\W+', '#@$VSCODE', 0, '#@$')
]

input_clean_termos = [
    (['   lalala', 'lala  ', '   lala lala'], ['lalala', 'lala', 'lala lala']),
    ('#$@string@#@', 'string')
]


@pytest.mark.parametrize("pattern, string, flags, saida", input_find_termo)
def test_find_termo(pattern, string, flags, saida):
    assert find_termo(pattern, string, flags) == saida


@pytest.mark.parametrize("termos, saida", input_clean_termos)
def test_clean_termos(termos, saida):
    assert clean_termos(termos) == saida

import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.parametrize('text, result', [
    ('python', 'Python'),
    ('Python', 'Python'),
    ('python python', 'Python python')
])
def test_capitalize_positive(text, result):
    string_utils = StringUtils()
    assert string_utils.capitalize(text) == result


@pytest.mark.parametrize('text, result', [
    ('', ''),
    ('111python', '111python'),
    ('   ', '   '),
])
def test_capitalize_negative(text, result):
    string_utils = StringUtils()
    assert string_utils.capitalize(text) == result


@pytest.mark.parametrize('text, result', [
    ('   python', 'python'),
    ('python', 'python'),
    (' Python', 'Python')
])
def test_trim_positive(text, result):
    string_utils = StringUtils()
    assert string_utils.trim(text) == result


@pytest.mark.parametrize('text, result', [
    ('', ''),
    ('   ', ''),
])
def test_trim_negative(text, result):
    string_utils = StringUtils()
    assert string_utils.trim(text) == result


@pytest.mark.parametrize('string, symbol, bool', [
    ('Python', 'y', True),
    ('Python', 'e', False),
    ('Python', 'P', True),
    ('Python', 'u', False)
])
def test_contains_positive(string, symbol, bool):
    string_utils = StringUtils()
    assert string_utils.contains(string, symbol) is bool


@pytest.mark.parametrize('string, symbol, bool', [
    ('', '', True),
    ('', 'y', False),
    ('   ', '   ', True),
    ('   ', 'u', False)
])
def test_contains_negative(string, symbol, bool):
    string_utils = StringUtils()
    assert string_utils.contains(string, symbol) is bool


@pytest.mark.parametrize('string, symbol, result', [
    ('Python', 'P', 'ython'),
    ('Python', 'on', 'Pyth'),
    ('Python', 'Python', '')
])
def test_delete_symbol_positive(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result


@pytest.mark.parametrize('string, symbol, result', [
    ('Python', 'q', 'Python'),
    ('', 's', ''),
    ('sss', 's', '')
])
def test_delete_symbol_negative(string, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(string, symbol) == result

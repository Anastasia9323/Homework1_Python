import pytest
from string_processor import StringProcessor

stringProcessor = StringProcessor()


@pytest.mark.parametrize('text, result', [
    ("Hello", "Hello."),
    ("hello", "Hello."),
    ("hello word", "Hello word."),
],
)
def test_positive(text, result):
    stringProcessor = StringProcessor()
    assert stringProcessor.process(text) == result


@pytest.mark.parametrize('text, result', [
    ('', '.'),
    ('   ', '   .'),
],
)
def test_negative(text, result):
    stringProcessor = StringProcessor()
    assert stringProcessor.process(text) == result

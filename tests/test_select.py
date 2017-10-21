from crosscompute_select import SelectType


X = SelectType
DEFAULT_VALUE = ['one', 'two'], []


def test_parse():
    assert X.parse('one', DEFAULT_VALUE) == (['one', 'two'], ['one'])
    assert X.parse('one\nthree', DEFAULT_VALUE) == (['one', 'two'], ['one'])


def test_render():
    x = 'one'
    assert X.render(X.parse(x, DEFAULT_VALUE)) == x

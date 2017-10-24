from crosscompute.exceptions import DataTypeError
from crosscompute_select import SelectType
from pytest import raises


X = SelectType
DEFAULT_VALUE = ['one', 'two'], []


def test_parse():
    assert X.parse('one', DEFAULT_VALUE) == (['one', 'two'], ['one'])
    with raises(DataTypeError):
        X.parse('one\nthree', DEFAULT_VALUE)


def test_render():
    x = 'one'
    assert X.render(X.parse(x, DEFAULT_VALUE)) == x

# test parsing
from crosscompute_select import SelectType

def test_spaces():
    text = '    \n    2   \n     5    \n'
    all_options, selected_options = SelectType.parse(text)
    assert all_options == ['2', '5']
    assert selected_options == []


def test_multi_newline():
    text = '\n\n2\n\n5\n\n4\n\n'
    all_options, selected_options = SelectType.parse(text)
    assert all_options == ['2', '5', '4']
    assert selected_options == []


def test_default():
    text = '\n*2*\n5\n*4*\n6\n'
    all_options, selected_options = SelectType.parse(text)
    assert all_options == ['2', '5', '4', '6']
    assert selected_options == ['2', '4']


def test_multi_stars():
    text = '\n**2**\n5\n**4**\n6\n'
    all_options, selected_options = SelectType.parse(text)
    assert all_options == ['*2*', '5', '*4*', '6']
    assert selected_options == ['*2*', '*4*']
    text = '\n**\n5\n**4**\n6\n'
    all_options, selected_options = SelectType.parse(text)
    assert all_options == ['5', '*4*', '6']
    assert selected_options == ['*4*']


def test_format():
    text = '\n*2*\n5\n*4*\n6\n'
    result = SelectType.parse(text)
    formatted_result = SelectType.render(result)
    assert formatted_result == '\n    2\n    4\n'

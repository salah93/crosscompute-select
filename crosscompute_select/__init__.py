from crosscompute.exceptions import DataTypeError
from crosscompute.types import DataType


class SelectType(DataType):

    suffixes = 'select', 'options'
    formats = 'txt',
    script = 'crosscompute_select:assets/part.min.js'
    template = 'crosscompute_select:type.jinja2'
    requires_value_for_path = True

    @classmethod
    def parse(Class, x, default_value=None):
        if isinstance(x, tuple):
            return x
        all_options, selected_options = [], []
        xs = selected_options
        for line in x.strip().splitlines():
            line = line.strip()
            if not line:
                xs = all_options
                continue
            xs.append(line)
        if default_value:
            all_options = default_value[0]
        elif not all_options:
            all_options = selected_options
        for x in selected_options:
            if x not in all_options:
                raise DataTypeError('invalid')
        return all_options, selected_options

    @classmethod
    def render(Class, value):
        selected_options = value[1]
        return '\n'.join(selected_options)

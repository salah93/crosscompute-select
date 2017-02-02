from crosscompute.types import DataType, DataTypeError


class SelectType(DataType):
    suffixes = 'select'
    # TODO: what is this
    # formats = 'txt',
    template = 'crosscompute_select:type.jinja2'

    @classmethod
    def parse(Class, text):
        """
        x_select = 
            x
            *y
            *z
        """
        all_options = [option.strip(' ,;') for option in text.split('\n')]
        default_options = filter(lamda x: x[0] == '*', all_options) 
        # return all options, default options
        return all_options, default_options

    @classmethod
    def format(Class, (all_options, default_options)):
        return '\n'.join(all_options)

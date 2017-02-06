from crosscompute.types import DataType


class SelectType(DataType):
    suffixes = 'select',
    template = 'crosscompute_select:type.jinja2'

    @classmethod
    def parse(Class, text):
        """
        x_select =
            x
            *y*
            *z
            **
        """
        all_options = []
        default_options = []
        lines = text.strip().split('\n')
        for option in lines: 
            option = option.strip(' ,;\n')
            if not option:
                continue
            if option[0] == '*' and option[-1] == '*':
                option = option[1:-1].strip(' ,;')
                if not option:
                    continue
                default_options.append(option)
            all_options.append(option)
        # return all options, default options
        return all_options, default_options

    @classmethod
    def format(Class, (all_options, default_options)):
        return '\n'.join(all_options)

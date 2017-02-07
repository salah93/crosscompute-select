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
        selected_options = []
        lines = text.strip().split('\n')
        for option in lines: 
            option = option.strip(' ,;\n')
            if not option:
                continue
            if option[0] == '*' and option[-1] == '*':
                option = option[1:-1].strip(' ,;')
                if not option:
                    continue
                selected_options.append(option)
            all_options.append(option)
        return all_options, selected_options

    @classmethod
    def format(Class, (all_options, selected_options)):
        # restar default options
        for i, option in enumerate(all_options):
            if option in selected_options:
                option = '*%s*' % option
            all_options[i] = option
        return '\n'.join(all_options)

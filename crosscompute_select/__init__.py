from crosscompute.types import DataType


class SelectType(DataType):

    suffixes = 'select',
    template = 'crosscompute_select:type.jinja2'

    @classmethod
    def parse(Class, text):
        """
        selected options will have '*' surrounding it
        other options will not

        x_select =
            x
            *y*
            *z*
            a
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
    def merge(Class, old_value, new_value):
        return old_value[0], new_value[0]

    @classmethod
    def render(Class, (all_options, selected_options)):
        ''' change two lists into a single string of items separated by
            new lines (format and parse are inverses of eachother'''
        return '\n'.join(selected_options)

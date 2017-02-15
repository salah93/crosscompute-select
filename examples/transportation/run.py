from argparse import ArgumentParser
from invisibleroads_macros.disk import make_enumerated_folder_for, make_folder
from invisibleroads_macros.log import format_summary


if __name__ == '__main__':
    argument_parser = ArgumentParser()
    argument_parser.add_argument(
        '--target_folder',
        metavar='FOLDER', type=make_folder)
    argument_parser.add_argument(
        '--mode',
        required=True)

    args = argument_parser.parse_args()
    print(type(args.mode))
    print(args.mode.split('\n'))

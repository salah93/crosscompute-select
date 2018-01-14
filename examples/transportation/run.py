from sys import argv

modes = argv[1].splitlines()
if len(modes) == 0:
    print("I don't like to move")
else:
    print('I like to move by %s' % ' and '.join(modes))

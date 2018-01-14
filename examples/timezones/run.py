from sys import argv


selected_timezones = argv[1].splitlines()
print('selected_timezones = %s' % ', '.join(selected_timezones))
print('timezone count = %d' % len(selected_timezones))

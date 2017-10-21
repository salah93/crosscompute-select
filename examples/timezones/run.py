from sys import argv


selected_timezones = argv[1].splitlines()
print('selected_timezones = %s' % ', '.join(selected_timezones))
print('selected_timezone_count = %s' % len(selected_timezones))

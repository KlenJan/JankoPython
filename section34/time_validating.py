import re

def is_valid_time(time_str):
    pattern = re.compile(r'^\d{1,2}:\d\d$')
    if pattern.search(time_str):
        return True
    return False
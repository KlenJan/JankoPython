import re

def parse_date(input_date_str):
    search_pattern = re.compile(r'(^\d\d)[/.,]{1}(\d\d)[/.,]{1}(\d{4})')
    result = search_pattern.search(input_date_str)
    if result:
        return {'d': result.group(1), 'm': result.group(2), 'y': result.group(3)}
    return None

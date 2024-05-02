import re

def parse_bytes(input_str):
    search_pattern = re.compile(r'\b[0-1]{8}\b')
    return search_pattern.findall(input_str)
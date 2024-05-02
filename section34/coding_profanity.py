import re

def censor(input_str):
    s_pattern = re.compile(r'\bfrack[a-z]*\b', re.I)
    result = s_pattern.sub("CENSORED", input_str)
    print(result)

censor("Frack you")
censor("I hope you fracking die")
def combine_words(word, **kwargs):
    if "prefix" in kwargs:
        word = f"{kwargs['prefix']}{word}"
    if "suffix" in kwargs:
        word = f"{word}{kwargs['suffix']}"
    return word

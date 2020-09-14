def search4letters(phrase:str="", letters:str='aeiou') -> set:
    """Returns set of letters which are interseption of letters and phrase sets"""
    return set(letters).intersection(set(phrase))

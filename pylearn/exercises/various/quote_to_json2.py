#! Программа quote to json.


def json_to_text(file='../quote_to_json2.json'):
    with open(file) as fo:
        text = fo.read()
    return text.split()


def set_library(text):
    lib = ''
    lib_start = text.index('<')
    lib_open = 1
    lib_close = 0
    order = 0
    for word in text[lib_start + 1:]:
        order += 1
        if word == '<':
            lib_open += 1
        elif word == '>':
            lib_close += 1
            if lib_open == lib_close:
                break
    lib_end = text.index('<') + order
    if '<' not in text or '>' not in text:
        lib = []
    elif len(text) == (lib_end + 1) and len(text) > 3:
        lib = [{"text": text[lib_start + 1],
               "children": [set_library(text[lib_start + 2: lib_end])]}]
    elif len(text) > (lib_end + 1) and (lib_end + 1) == 3:
        lib = [{"text": text[lib_start + 1],
                "children": []}, set_library(text[lib_end + 1:])]
    elif len(text) > (lib_end + 1) and (lib_end + 1) > 3:
        lib = [{"text": text[lib_start + 1],
                "children": [set_library(text[lib_start + 2: lib_end])]},
              set_library(text[lib_end + 1:])]
    return lib


a = [1, 2, 3, 4, 5]

print(a[:4])

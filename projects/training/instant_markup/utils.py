"""A Text Block Generator"""

def lines(file):
    """Lines generator"""
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    """Blocks generator"""
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


print("Suplier      Amount      Count".strip())
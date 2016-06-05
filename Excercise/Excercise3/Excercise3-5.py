def draw_grid(n):
    for i in range(n):
        print_block(n)

    print hor_block(n)


def hor_block(n):
    hor_str = "+"
    extend_str = "----+"
    for i in range(4):
        hor_str += '-'

    hor_str += '+'
    j = 1
    while j < n:
        hor_str += extend_str
        j += 1

    return hor_str


def ver_block(n):
    ver_str = "|"
    extend_str = "    |"
    for i in range(4):
        ver_str += ' '

    ver_str += '|'

    j = 1

    while j < n:
        ver_str += extend_str
        j += 1

    return ver_str


def print_block(n):
    print hor_block(n)
    print ver_block(n)
    print ver_block(n)
    print ver_block(n)
    print ver_block(n)


draw_grid(6)

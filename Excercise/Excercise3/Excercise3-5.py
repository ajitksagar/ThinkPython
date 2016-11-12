def draw_grid(n):
    for i in range(n):
        print_block(n)

    print hor_line(n)


def print_block(n):
    print hor_line(n)
    print ver_line(n)
    print ver_line(n)
    print ver_line(n)
    print ver_line(n)


def hor_line(n):
    hor_str = "+----+"
    extend_str = "----+"

    j = 1
    while j < n:
        hor_str += extend_str
        j += 1

    return hor_str


def ver_line(n):
    ver_str = "|    |"
    extend_str = "    |"

    j = 1

    while j < n:
        ver_str += extend_str
        j += 1

    return ver_str


draw_grid(5)

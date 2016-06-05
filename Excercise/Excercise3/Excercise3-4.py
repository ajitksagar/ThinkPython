def do_twice(f,name):
    f(name)

def do_four(f,string):
    f(string)

def print_twice(name):
    print name
    print name

def print_fourtimes(string):
    print string
    print string
    print string
    print string


do_twice(print_twice,'ajit')

do_four(print_fourtimes,'kshirsagar')
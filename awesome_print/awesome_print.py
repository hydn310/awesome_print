""" Attempt to clone https://github.com/michaeldv/awesome_print

Usage:
    from awesome_print import ap
    ap(object)
"""
from __future__ import print_function
from types import LambdaType

try:
    basestring
    def is_str(s):
        return isinstance(s, basestring)
except NameError:
    def is_str(s):
        return isinstance(s, str)

try:
    long
    def is_num(n):
        return isinstance(n, (int, long, float, complex))
except NameError:
    def is_num(n):
        return isinstance(n, (int, float, complex))

mode = 'ansi'

def ap(*args):
    for arg in args:
        print(format(arg))

def indent(level):
    return '  ' * level

def format(obj, level = 0):
    if obj is None:
        return red('None')

    if isinstance(obj, bool):
        return green(str(obj))

    if is_str(obj):
        return yellow(str(obj))

    if is_num(obj):
        return bold_blue(str(obj))

    if isinstance(obj, (list, tuple)):
        open, close = ('(', ')') if isinstance(obj, tuple) else ('[', ']')
        if len(obj) is 0:
            return open + close

        s = []
        i = 0
        width = str(len(str(len(obj))))
        for e in obj:
            s.append(('%s[%' + width + 'd] %s') % \
                    (indent(level + 1), i, format(e, level + 1)))
            i+=1

        return open + "\n" + \
                        ",\n".join(s) + \
               "\n" + indent(level) + close

    if isinstance(obj, dict):
        if len(obj) is 0:
            return '{}'

        width = str(max([flen(format(k)) for k in obj.keys()]))
        s = []
        for k in obj.keys():
            v = obj[k]
            s.append(('%s%' + width + 's: %s') % \
                    (indent(level + 1), format(k), format(v, level + 1)))

        return '{' + "\n" + \
                        ",\n".join(s) + \
               "\n" + indent(level) + '}'

    if type(obj) is LambdaType:
        return str(obj)

    return str(obj)

def flen(str):
    return max(len(s) for s in str.split("\n"))

def black(str):
    return color(str, '30')

def dark_gray(str):
    return bold(str, '30')

def red(str):
    return color(str, '31')

def bold_red(str):
    return bold(str, '31')

def green(str):
    return color(str, '32')

def green(str):
    return bold(str, '32')

def yellow(str):
    return color(str, '33')

def bold_yellow(str):
    return bold(str, '33')

def blue(str):
    return color(str, '34')

def bold_blue(str):
    return bold(str, '34')

def purple(str):
    return color(str, '35')

def bold_purple(str):
    return bold(str, '35')

def cyan(str):
    return color(str, '36')

def bold_cyan(str):
    return bold(str, '36')

def light_gray(str):
    return color(str, '37')

def white(str):
    return bold(str, '37')

def color(str, color, intensity='0'):
    if mode == 'plain':
    	return str
    return '\033['+intensity+';'+color+'m'+str+'\033[0m'

def bold(str, col):
    if mode == 'plain':
    	return str
    return color(str, col, '1')

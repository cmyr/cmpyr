import re


def remove_ansi(string):
    return re.sub(r'\033\[[0-9]+m', '', string)


def ansi_ljust(string, count, fillchar=' '):
    naked_len = len(remove_ansi(string))
    if naked_len < count:
        string = '%s%s' % (string, fillchar*(count-naked_len))
    return string


class Colorize(object):
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    LIGHT_PURPLE = '\033[34m'
    PURPLE = '\033[35m'
    UNDER = '\033[4m'
    BOLD = '\033[1m'
    END = '\033[0m'

    @classmethod
    def red(cls, s):
        return "%s%s%s" % (cls.RED, s, cls.END)

    @classmethod
    def green(cls, s):
        return "%s%s%s" % (cls.GREEN, s, cls.END)

    @classmethod
    def yellow(cls, s):
        return "%s%s%s" % (cls.YELLOW, s, cls.END)

    @classmethod
    def light_purple(cls, s):
        return "%s%s%s" % (cls.LIGHT_PURPLE, s, cls.END)

    @classmethod
    def purple(cls, s):
        return "%s%s%s" % (cls.PURPLE, s, cls.END)

    @classmethod
    def bold(cls, s):
        return "%s%s%s" % (cls.BOLD, s, cls.END)

    @classmethod
    def under(cls, s):
        return "%s%s%s" % (cls.UNDER, s, cls.END)

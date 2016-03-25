import math

def format_seconds(seconds):
    """
    convert a number of seconds into a custom string representation
    """
    d, seconds = divmod(seconds, (60 * 60 * 24))
    h, seconds = divmod(seconds, (60 * 60))
    m, seconds = divmod(seconds, 60)
    time_string = ("%im %0.2fs" % (m, seconds))
    if h or d:
        time_string = "%ih %s" % (h, time_string)
    if d:
        time_string = "%id %s" % (d, time_string)
    return time_string


def format_size(size):
    """ taken verbatim from http://stackoverflow.com/a/14822210/1529922"""
    size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
    if size == 0:
        return '0B'
    i = int(math.floor(math.log(size, 1024)))
    p = math.pow(1024, i)
    s = round(size/p, 2)
    if (s > 0):
        return '%s %s' % (s, size_name[i])
    else:
        return '0B'

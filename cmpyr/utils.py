import sys
from datetime import datetime


def timeprint(message):
    sys.stdout.write("%s: %s\n" % (datetime.utcnow().strftime('%H:%M:%S'), message))
    sys.stdout.flush()


def prune_dict(indict, dict_template):
    """
    given two dictionaries, returns a new dictionary with those key/value
    pairs from the first dictionary that are present in the second. If value
    is a dictionary, performs recursively.
    """

    outdict = dict()
    for key, value in dict_template.items():
        keep = indict.get(key)
        if isinstance(keep, dict) and isinstance(value, dict):
            outdict[key] = prune_dict(keep, value)
        else:
            outdict[key] = keep
    return outdict

import sys
from datetime import datetime


def timeprint(message):
    sys.stdout.write("%s: %s\n" % (datetime.utcnow().strftime('%H:%M:%S'), message))
    sys.stdout.flush()

import os
import sys
import time
import json
import gzip

from . import string_utils


def iter_dir(path, item_filter=None, recursive=True, batch=False, verbosity=0):
    total_files = len(recursive_find_files(path))
    current_file = 0
    start_time = time.time()

    for root, dirs, files in os.walk(path):
        if verbosity > 1:
            print('root %s' % root)
            print('dirs %s' % dirs)
            print('files %s' % files)
        if not recursive:
            total_files = len(files)
            dirs = list()
        # we ignore things that start with an undarbar '_'
        baddirs = [d for d in dirs if d.startswith(('_', '.'))]
        for b in baddirs:
            del dirs[dirs.index(b)]

        for f in [f for f in files if not f.startswith(('_', '.'))]:
            if verbosity > 0 and current_file > 0:
                elapsed = time.time() - start_time
                t_remaining = (
                    elapsed / max(current_file, 1)) * (total_files - current_file)
                sys.stdout.write('\rprocessing file %d/%d. %s remaining'
                                 % (current_file, total_files, string_utils.format_seconds(t_remaining)))
                sys.stdout.flush()
            if verbosity > 1:
                print(os.path.join(root, f))
            current_file += 1
            for item in iter_file(os.path.join(root, f), item_filter):
                try:
                    yield item
                except StopIteration:
                    continue
    if verbosity:
        print('\nfinished with %d files in %s' %
              (total_files, string_utils.format_seconds(time.time() - start_time)))


def recursive_find_files(basepath):
    all_files = list()
    for root, dirs, files in os.walk(basepath):
        ignore = [d for d in dirs if d.startswith(('_', '.'))]
        for i in ignore:
            dirs.remove(i)
        all_files.extend(
            os.path.join(root, f) for f in files if not f.startswith(('_', '.')))
    return [f for f in all_files if f.endswith('gz')]


def load_gzip_json(path, item_filter=None):
    if path.endswith('gz'):
        try:
            f = gzip.open(path, 'rb')
            items = json.loads(f.read().decode('utf-8'))
            f.close()
        except (OSError, ValueError) as err:
            print(err)
            print('ERROR WITH FILE: %s' % path)
            return []
        except Exception as err:
            print(err)
            print('OTHER ERROR WITH FILE %s' % path)
            return []
        # shared.dprint("loaded %d items from %s" % (len(items), path), 1)
        if item_filter:
            return [item_filter(i) for i in items]
        else:
            return items
    else:
        print("skipping file %s" % path)


def iter_file(path, item_filter=None):
    items = load_gzip_json(path, item_filter) or list()
    for i in items:
        yield i
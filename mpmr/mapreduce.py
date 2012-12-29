import sys

def do_map(map_func):
    for line in sys.stdin:
        tks = line.strip().split('\t')
        key = tks[0]
        value = '\t'.join(tks[1:])
        map_func(key, value)

def do_reduce(reduce_func):
    prev_key = ''
    values = []
    for line in sys.stdin:
        tks = line.strip().split('\t')
        key = tks[0]
        value = '\t'.join(tks[1:])

        if prev_key != key:
            if len(prev_key) > 0:
                reduce_func(key, values)
            prev_key = key
            values = []
        values.append(value)

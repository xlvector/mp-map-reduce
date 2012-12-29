import mpmr.mapreduce
import sys

def map_func(key, value):
    words = value.split(' ')
    for word in words:
        print word + '\t1'

def reduce_func(key, values):
    print key + '\t' + sum([int(x) for x in values])

if sys.argv[1] == 'map':
    mpmr.mapreduce.do_map(map_func)
elif sys.argv[1] == 'reduce':
    mpmr.mapreduce.do_reduce(reduce_func)

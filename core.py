# imports a bit of a problem, the incur a startup cost even if they are not
# used. I need to find a way to minimize this by making them load lazily. Or
# perhaps by "shaking the tree" and/or compiling the code.
import time
import copy

def mlc_elem(x, xs):
    return x in xs

def mlc_run(f):
    return f()

def mlc_neg(x):
  return (-1) * x

def mlc_id(x):
  return x

def mlc_at(i, xs):
  return xs[i]

def mlc_enumerateWith(f, xs):
  for (x,i) in enumerate(xs):
    yield f(x,i)

def mlc_fold(f, b, xs):
  for x in xs:
    b = f(b, x)
  return b

def mlc_add(a,b):
  return a+b

def mlc_sub(a,b):
  return a-b

def mlc_mul(a,b):
  return a*b

def mlc_div(a,b):
  return a/b

def mlc_map(f, *args):
  return list(map(f, *args))

def mlc_filter(f, xs):
    return [x for x in xs if f(x)]

def mlc_fst(x):
  return x[0]

def mlc_snd(x):
  return x[0]

def mlc_thr3(x):
  return x[2]

#  onFst :: (a -> a') -> (a, b) -> (a', b)
def mlc_onFst(f, x):
    return(f(x[0]))

#  concat :: [[a]] -> [a]
def mlc_concat(xss):
    ys = []
    for xs in xss: 
        ys.append(xs)
    return ys

#  sleep py :: Real -> a -> a
def mlc_sleep(n, a):
    time.sleep(n)
    return a

#  shard py :: Int -> [a] -> [[a]]
def mlc_shard(chunkSize, xs):
    if(len(xs) == 0):
        return [[]]
    else:
        xss = []
        for i in range(1, len(xs) + 1):
            if i % chunkSize == 0:
                xss.append(xs[i - chunkSize: i])
        size = chunkSize * (len(xs) // chunkSize)
        if size < len(xs):
            xss.append(xs[size - 1: len(xs)])
    return xss

#  join py :: [a] -> [a] -> [a]
def mlc_join(xs, ys):
    # this function should not mutate the data
    xsCopy = copy.copy(xs)
    xsCopy.append(ys)
    return xsCopy

def mlc_filterKey(cond, d):
    return {k:v for (k, v) in d.items() if cond(k)}

def mlc_filterVal(cond, d):
    return {k:v for (k, v) in d.items() if cond(v)}

def mlc_keys(d):
    return list(d.keys())

def mlc_vals(d):
    return list(d.values())

def mlc_gt(x, y):
	return x > y

def mlc_lt(x, y):
	return x < y

def mlc_ge(x, y):
	return x >= y

def mlc_le(x, y):
	return x <= y

def mlc_eq(x, y):
	return x == y

def mlc_ne(x, y):
	return x != y

def mlc_not(x):
	return (not x)

def mlc_and(x, y):
	return (x and y)

def mlc_or(x, y):
	return (x or y)

def mlc_readMap(filename):
    x = dict()
    with open(filename, "r") as f:
        for line in f.readlines():
            (k,v) = line.split("\t")
            x[k] = v
        return x

def mlc_seq(a, b):
    return b

def mlc_const(a, b):
    return a

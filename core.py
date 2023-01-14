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

def mlc_fst(x):
  return x[0]

def mlc_snd(x):
  return x[0]

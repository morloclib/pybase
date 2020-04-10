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

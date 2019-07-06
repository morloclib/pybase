def enumerateWith(f, xs):
  for (x,i) in enumerate(xs):
    yield f(x,i)

def fold(f, b, xs):
  for x in xs:
    b = f(b, x)
  return b

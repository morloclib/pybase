def enumerateWith(f, xs):
  for (x,i) in enumerate(xs):
    yield f(x,i)

def fold(f, b, xs):
  for x in xs:
    b = f(b, x)
  return b

def add(a,b):
  return a+b

def sub(a,b):
  return a-b

def mul(a,b):
  return a*b

def div(a,b):
  return a/b

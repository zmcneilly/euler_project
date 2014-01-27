#!env/bin/python

def isodd(num):
  return num & 1 and True or False

def fib(n):
  "Return a Fibonacci result at n"
  a, b, i = 0, 1, 0
  while i < n:
    a, b = b, a+b
    i += 1
  return b

total = 0
for x in range(1,4000000,1):
  res = fib(x)
  if not(isodd(res)) and res <= 4000000:
    total += res
  if res > 4000000:
    break

print total

# The Karatsuba algorithm is a fast "Divide and Conquer" multiplication algorithm.
# It was published by Anatoly Karatsuba in 1962.
# This Python implementation calculates the product of two n-bit numbers in O(n^1.58)
# It works completely without using Python's "*"-operator; just "+", "-", bitwise operations and a lookup table.

lookuptable = {
  (-1,-1): 1, (-1,0): 0, (-1, 1): -1,
  (0,-1): 0, (0,0):0, (0,1): 0,
  (1,-1): -1, (1,0): 0, (1,1): 1}


def karatsuba(x,y):
  n = max(x.bit_length(), y.bit_length())

  # trivial
  if n <= 1:
    return lookuptable[(x, y)]

  # divide
  k = (n + 1) >> 1
  x1 = x >> k
  x0 = x - (x1 << k)
  y1 = y >> k
  y0 = y - (y1 << k)

  # recursions
  a = karatsuba(x1, y1)
  c = karatsuba(x0, y0)
  p = karatsuba(x0 + x1, y0 + y1)
  b = p - a - c

  # conquer
  return (a << (n + (n & 1))) + (b << (k)) + c
  

print(karatsuba(-1, 1))
print(karatsuba(200, 200))
print(karatsuba(21233212313124121123123212213212121332123132122123321231312412112312321221321212133212313212, 2321313122133121321323211232131213231231231212142123321231312412112312321221321212133212313212))
print(karatsuba(-29, 31))
import subprocess
import numpy as np

BOW = "<"
EOW = ">"

def hash2(ss):
  return subprocess.call(["./hash.out", ss])

M32 = 0xffffffffL
def m32(n):
  return n & M32
def madd(a, b):
  return m32(a+b)
def msub(a, b):
  return m32(a-b)
def mls(a, b):
  return m32(a<<b)
def mmul(a, b):
  return m32(a*b)

def mpower(a,b):
  if b == 0:
    return 1;
  elif b == 1:
    return a;
  else:
    res = mpower(a, b/2)
    val = mmul(res, res)
    if b % 2 == 0:
      return val
    else:
      return mmul(val, a)

def hash(str):
  h = m32(2166136261L)
  for c in str:
    cc = m32(long(ord(c)))
    h = m32(h ^ cc)
    h = mmul(h, 16777619L)
  return h
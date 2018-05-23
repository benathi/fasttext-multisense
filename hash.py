import subprocess
import numpy as np

# BenA:
# the constant values here reflect the values in original FastText implementation

BOW = "<"
EOW = ">"

M32 = 0xffffffffL

def m32(n):
  return n & M32

def mmul(a, b):
  return m32(a*b)

def hash(str):
  h = m32(2166136261L)
  for c in str:
    cc = m32(long(ord(c)))
    h = m32(h ^ cc)
    h = mmul(h, 16777619L)
  return h
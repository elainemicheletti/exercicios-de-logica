#!/usr/bin/python -tt
# coding: utf-8
import unittest

def verbing(s):
  if "ing" in s:
    return s + "ly"
  elif len(s) >= 3:
    return s + "ing"
  else:
    return s

# (google solution)
def verbingV2(s):
  if len(s) >= 3:
    if s[-3:] != 'ing': s = s + 'ing'
    else: s = s + 'ly'
  return s

def not_bad(s):
  n = s.find('not')
  b = s.find('bad')
  if n != -1 and b != -1 and b > n:
    s = s[:n] + 'good' + s[b+3:]
  return s

def front_back(a, b):
  a_middle = int(len(a) / 2)
  b_middle = int(len(b) / 2)

  # adiciona 1 se o tamanho for ímpar
  if len(a) % 2 == 1:
    a_middle = a_middle + 1

  if len(b) % 2 == 1:
    b_middle = b_middle + 1

  return a[:a_middle] + b[:b_middle] + a[a_middle:] + b[b_middle:]

class MyTest(unittest.TestCase):

  def test_verbing(self):
    self.assertEqual(verbing('hail'), 'hailing')
    self.assertEqual(verbing('swiming'), 'swimingly')
    self.assertEqual(verbing('do'), 'do')

  def test_not_bad(self):
    self.assertEqual(not_bad('This movie is not so bad'), 'This movie is good')
    self.assertEqual(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    self.assertEqual(not_bad('This tea is not hot'), 'This tea is not hot')
    self.assertEqual(not_bad("It's bad yet not"), "It's bad yet not")

  def test_front_back(self):
    self.assertEqual(front_back('abcd', 'xy'), 'abxcdy')
    self.assertEqual(front_back('abcde', 'xyz'), 'abcxydez')
    self.assertEqual(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  unittest.main()
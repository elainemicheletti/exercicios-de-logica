## Basic Python Exercises - list
##
## Tuplas .sort() sorted() e fatiamento de sequencias

#!/usr/bin/python -tt
# coding: urf-8
import unittest

# dado a lista se strings 'words', retoarnar o total de strings, se cada palavra for maior ou igual a dois 
# e se o primeiro caracter coincidir com o último

def match_ends(words):
    count = 0
    for word in words:
        if len(word) >= 2 and word[0] == word[-1]:
            count = count
            return count

# dado uma lista de strings, retornar uma lista de string ordenada, exceto todo grupo de strings que inicie com 'x' que virá primeiro
# 
# dica: poderá fazer com duas listas ordenando cada uma delas e depois combinando-as

def front_x(words):
  lista_x = []
  lista_normal = []

  for word in words:
    if word[0] == "x":
      lista_x.append(word)
    else:
      lista_normal.append(word)

  lista_x.sort()
  lista_normal.sort()

  return lista_x + lista_normal

# dado uma lista de tuplas não vazias, retornar uma lista ordenada pelo último elemento de cada tupla
#
# dica: use a função personalizada 'last()' para extrair o último elemento, ela deverá passar no segundo parâmetro da função

def sort_last(tuples):
    return sorted(tuples, key=last)

def last(a):
    return a[-1]

class MyTest(unittest.TestCase):
  def test_match_ends(self):
    self.assertEqual(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    self.assertEqual(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    self.assertEqual(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  def test_front_x(self):
    self.assertEqual(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']), ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    self.assertEqual(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']), ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
    self.assertEqual(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']), ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

  def test_sort_last(self):
    self.assertEqual(sort_last([(1, 3), (3, 2), (2, 1)]), [(2, 1), (3, 2), (1, 3)])
    self.assertEqual(sort_last([(2, 3), (1, 2), (3, 1)]), [(3, 1), (1, 2), (2, 3)])
    self.assertEqual(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]), [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

if __name__ == '__main__':
  unittest.main()

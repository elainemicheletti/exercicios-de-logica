## Basic Python Exercices - strings
##
## Funções e estrutura if



#!/usr/bin/python -tt
# coding: utf-8
import unittest

# dado count, retornar uma string na forma "Numero de donuts: ,count>", caso count seja maior igual a dez, retornar "many"

def donuts(count):
    if count < 10:
        return 'Numero de donuts: ' + str(count)
    else:
        return 'Numero de donuts: many'

def donutsV2(count):
    if count < 10:
        count = str(count)
    else:
        count = "many"
        return 'Numero de donuts: %s' % count

# dado a string 's', retornar uma string composta por dois primeiros e dois últimos caracteres
# 
# caso a string 's' contenha menos que dois caracteres, retornar ""

def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

# dado a string 's', retornar uma string onde todas as ocorrências de seu primeiro caracter alterado para '*', exceto o primeiro caracter
#
# considere que o tamanho da string seja um ou mais
#
# dica: s.replace (stra, strb) retorna uma versão da string s

def fix_start(s):
    front = s[0]
    back = s[1:]
    fixed_back = back.replace(front, '*')
    return front + fixed_back

# dado as strings 'a' e 'b', trocar os dois primeiros caracteres entre as variáveis e retornar uma única string separada por espaço

def mix_up(a, b):
    a_swapped = b[:2] + a[2:]
    b_swapped = a[:2] + b[2:]
    return a_swapped + ' ' + b_swapped

class MyTest(unittest.TestCase):

    def test_donuts(self):
      self.assertEqual(donuts(4), 'Number of donuts: 4')
      self.assertEqual(donuts(9), 'Number of donuts: 9')
      self.assertEqual(donuts(10), 'Number of donuts: many')
      self.assertEqual(donuts(99), 'Number of donuts: many')

    def test_both_ends(self):
      self.assertEqual(both_ends('spring'), 'spng')
      self.assertEqual(both_ends('Hello'), 'Helo')
      self.assertEqual(both_ends('a'), '')
      self.assertEqual(both_ends('xyz'), 'xyyz')
      self.assertEqual(both_ends('xy'), 'xyxy')

    def test_fix_start(self):
      self.assertEqual(both_ends('xy'), 'xyxy')
      self.assertEqual(fix_start('babble'), 'ba**le')
      self.assertEqual(fix_start('aardvark'), 'a*rdv*rk')
      self.assertEqual(fix_start('google'), 'goo*le')
      self.assertEqual(fix_start('donut'), 'donut')

    def test_mix_up(self):
      self.assertEqual(mix_up('mix', 'pod'), 'pox mid')
      self.assertEqual(mix_up('dog', 'dinner'), 'dig donner')
      self.assertEqual(mix_up('gnash', 'sport'), 'spash gnort')
      self.assertEqual(mix_up('pezzy', 'firm'), 'fizzy perm')

if __name__ == '__main__':
  unittest.main()
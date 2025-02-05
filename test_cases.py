#!/usr/bin/python3

import unittest
from calc_mul import calc

# Run with testrunner so needs to be in file test_

class TestCalc (unittest.TestCase):

        def test_sample01 (self): # 入力Aの方が大きい
                self.assertEqual (250500, calc(501,500))

        def test_sample02 (self): # 入力Bの方が大きい
                self.assertEqual (250500, calc(500,501))

        def test_sample03 (self): # 中央値同士
                self.assertEqual (250000, calc(500,500))

        def test_sample04 (self): # 最小値同士
                self.assertEqual (1, calc(1,1))

        def test_sample05 (self): # 最大値同士
                self.assertEqual (998001, calc(999,999))

        def test_sample06 (self): # 最小値と最大値
                self.assertEqual (999, calc(1,999))
                self.assertEqual (999, calc(999,1))

        def test_sample07 (self): # 最小値の境界外を含む
                self.assertEqual (-1, calc(0,1))
                self.assertEqual (-1, calc(1,0))

        def test_sample08 (self): # 最大値の境界外を含む
                self.assertEqual (-1, calc(1000,999))
                self.assertEqual (-1, calc(999,1000))

        def test_sample09 (self): # 境界外同士
                self.assertEqual (-1, calc(0,1000))

        def test_sample10 (self): # 小数同士
                self.assertEqual (-1, calc(1.1,1.1))

        def test_sample11 (self): # 小数を含む
                self.assertEqual (-1, calc(1.1,1))
                self.assertEqual (-1, calc(1,1.1))

        def test_sample12 (self): # 値なし同士
                self.assertEqual (-1, calc(None,None))

        def test_sample13 (self): # 値なしを含む
                self.assertEqual (-1, calc(None,1))
                self.assertEqual (-1, calc(1,None))

        def test_sample14 (self): # 整数の文字列
                self.assertEqual (999, calc('1','999'))

        def test_sample15 (self): # 文字列
                self.assertEqual (-1, calc('abc','abc'))

        def test_sample16 (self): # 後ろに文字列を含む
                self.assertEqual (-1, calc('1abc',1))
                self.assertEqual (-1, calc(1,'1abc'))

        def test_sample17 (self): # 前に文字列を含む
                self.assertEqual (-1, calc('abc1',1))
                self.assertEqual (-1, calc(1,'abc1'))

        def test_sample18 (self): # 負の数同士
                self.assertEqual (-1, calc(-1,-1))

        def test_sample19 (self): # 負の数を含む
                self.assertEqual (-1, calc(-1,1))
                self.assertEqual (-1, calc(1,-1))

        def test_sample20 (self): # 0同士
                self.assertEqual (-1, calc(0,0))

        def test_sample21 (self): # 0.0同士
                self.assertEqual (-1, calc(0.0,0.0))

        def test_sample22 (self): # True同士
                self.assertEqual (-1, calc(True,True))

        def test_sample23 (self): # TrueとFalse
                self.assertEqual (-1, calc(True,False))
                self.assertEqual (-1, calc(False,True))

        def test_sample24 (self): # Trueを含む
                self.assertEqual (-1, calc(True,1))
                self.assertEqual (-1, calc(1,True))

        def test_sample25 (self): # Falseを含む
                self.assertEqual (-1, calc(False,1))
                self.assertEqual (-1, calc(1,False))
import pytest
from unittest import TestCase

from crossroads import Crossroads


class TestCrossroadsHelper(TestCase):

  def testIsBlockingTiebreaker(self):
    crossroads = Crossroads()

    results = crossroads.isBlocking(75, 75)

    self.assertEqual(True, results)


  def testIsBlocking1(self):
    crossroads = Crossroads()

    results = crossroads.isBlocking(85, 20)

    self.assertEqual(True, results)


  def testIsBlocking2(self):
    crossroads = Crossroads()

    results = crossroads.isBlocking(20, 85)

    self.assertEqual(False, results)



class TestCrossroads(TestCase):

  def test1(self):
    crossroads = Crossroads()
    angles     = [105, 75, 25, 120, 35, 75]

    passedCars = crossroads.getOut(angles)

    self.assertEqual([0, 1, 5], passedCars)


  def test2(self):
    """
    If the two cars' paths have congruent angles, then they all should pass.
    """

    crossroads = Crossroads()
    angles     = [1, 1, 1, 1, 1, 1]

    passedCars = crossroads.getOut(angles)

    self.assertEqual([0, 1, 2, 3, 4, 5], passedCars)


  def test3(self):
    crossroads = Crossroads()
    angles     = [90, 123, 1, 23, 132, 11, 28, 179, 179, 77, 113, 91]

    passedCars = crossroads.getOut(angles)

    self.assertEqual([0], passedCars)


  def test4(self):
    crossroads = Crossroads()
    angles     = [179, 89, 90, 91, 1]

    passedCars = crossroads.getOut(angles)

    self.assertEqual([0, 2, 4], passedCars)


  def test5(self):
    crossroads = Crossroads()
    angles     = [89, 91]

    passedCars = crossroads.getOut(angles)

    self.assertEqual([0], passedCars)


  def test6(self):
    crossroads = Crossroads()
    angles = [140, 118, 54, 166, 151, 44 , 90 , 5,  14,  6  ,
               64, 129, 74, 33 , 134, 25 , 11 , 95, 65,  145,
               29, 162, 24, 147, 45 , 103, 63 , 97, 120, 156,
              167, 170, 19, 28 , 100, 144, 161, 13, 157, 148]

    passedCars = crossroads.getOut(angles)

    self.assertEqual([0, 1, 6], passedCars)

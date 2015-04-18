import math


class Crossroads(object):

  # Returns all cars which passes through. Cars are identified by array indices.
  def getOut(self, angles):
    passedCars  = []
    blockedCars = [] # closed set implementation. TODO: How to implement const.
                     # access?
    lastCar     = len(angles)

    for currCar in range(0, lastCar):
      if (currCar in blockedCars):
        continue

      isPassing = True

      for nextCar in range(currCar+1, lastCar):
        currCarAngle = angles[currCar]
        nextCarAngle = angles[nextCar]

        if self.hasNoIntersection(currCarAngle, nextCarAngle):
          pass
        else:
          if self.isBlocking(currCarAngle, nextCarAngle):
            blockedCars.append(nextCar)
          else:
            isPassing = False
            break

      if isPassing:
        passedCars.append(currCar)

    return passedCars


  def hasNoIntersection(self, angleA, angleB):
    return (angleA - angleB) >= 0


  def isBlocking(self, carAngleA, carAngleB):
    return abs(carAngleA - 90) <= abs(carAngleB - 90)



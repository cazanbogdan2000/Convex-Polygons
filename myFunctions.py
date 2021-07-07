# takes as a parameter a free vector, which is represented by a tuple, and print
# the free vector with i and j, and generate a representative vector
from random import random
from math import sqrt

# simple function to print the free vector and a representative vector for it
# also treats the cases when the projection on Ox or Oy is 0(then we don't
# print anything) or the projection is 1(and we print only "i" or "j")
def printVectors(vector):
    print("Free vector is: ", end = "")
    if vector[0] == 0:
        if vector[1] == 0:
            print(0)
        elif vector[1] == 1:
            print("j")
        else:
            print(str(vector[1]) + "j")
    else:
        if vector[0] == 1:
            print("i ", end = "")

        else:
            print(str(vector[0]) + "i ", end = "")
        if vector[1] == 0:
            print()
            pass
        elif vector[1] > 0:
            print("+ " + str(vector[1]) + "j")
        else:
            print("- " + str(-vector[1]) + "j")


    [(startingX, startingY), (endingX, endingY)] =\
        getRepresentativeFromFree(vector)

    print("A representative vector has the following starting and"
        " ending points: A(" + str(startingX) + "," + str(startingY) + "), "
        "B(" + str(endingX) + "," + str(endingY) + ")")

# Function that obtains a free vector by generating a random starting point
# between (0, 10) and then finding the ending point
# @return a list of 2 tuples with 2 numbers each one, first tuple is starting
# point, and the second one is the ending point
def getRepresentativeFromFree(vector):
    # generating 2 random integers from 0 to 10 to initialize a starting point
    # for our representative vector
    startingX = int(random() * 10)
    startingY = int(random() * 10)
    # the ending point is going to be found from the free vector and starting
    # coordinates, applying the formula:
    # (x2 - x1)i + (y2 - y1)j = x*i + y*j, where A(x1,y1), B(x2,y2) -> starting
    # and ending points of the representative vector, and (x, y) -> free vector
    endingX = vector[0] + startingX;
    endingY = vector[1] + startingY;
    return [(startingX, startingY), (endingX, endingY)]

# Function that simply obtains a free vector from a given representative vector
# The parameter is a list of tuples (representative vector)
# @return a tuple with 2 elements, which are the oriented projections of the
# obtained free vector
def getFreeFromRepresentative(vector):
    # get the starting and the endig points, with its coordinates
    startingPoint = vector[0]
    endingPoint = vector[1]
    # get the projections on Ox, respectively on Oy axes, applying the formula
    #explained also in the getRepresentativeFromFree function
    xProjection = endingPoint[0] - startingPoint[0]
    yProjection = endingPoint[1] - startingPoint[1]
    return (xProjection, yProjection)

# Function that translates a representative vector to an other representative
# vector, by 2 given parameters, dx and dy
# Note that the free vector stays the same, because we only translate the vector
# and not changing its length or direction
# @return the new translated representative vector
def translateVector(vector, dx, dy):
    # get the starting and the endig points, with its coordinates
    startingPoint = vector[0]
    endingPoint = vector[1]
    # now get the current coordinates og the starting point, and also of the
    # ending point
    xStarting = startingPoint[0]
    yStarting = startingPoint[1]
    xEnding = endingPoint[0]
    yEnding = endingPoint[1]
    # and we finally create the new coordinates of the translated vector
    xStartingNew = xStarting + dx;
    yStartingNew = yStarting + dy;
    xEndingNew = xEnding + dx;
    yEndingNew = yEnding + dy;
    return [(xStartingNew, yStartingNew), (xEndingNew, yEndingNew)]

# Function that calculates the sum of two free vectors
# @return a tuple which represent a new vector = vector1 + vector2
def addFreeVectors(vector1, vector2):
    xProjection1 = vector1[0]
    yProjection1 = vector1[1]
    xProjection2 = vector2[0]
    yProjection2 = vector2[1]
    xProjectionResult = xProjection1 + xProjection2
    yProjectionResult = yProjection1 + yProjection2
    return (xProjectionResult, yProjectionResult)

# Function that calculates the difference of two free vectors
# @return a tuple which represent a new vector = vector1 - vector2
def substractFreeVectors(vector1, vector2):
    xProjection1 = vector1[0]
    yProjection1 = vector1[1]
    xProjection2 = vector2[0]
    yProjection2 = vector2[1]
    xProjectionResult = xProjection1 - xProjection2
    yProjectionResult = yProjection1 - yProjection2
    return (xProjectionResult, yProjectionResult)

# Function that calculates the sum of two representative vectors
# Pay attention, because the result will be the free vector corresponding to
# the input
# @return a tuple which represents the resulted free vector
def addRepresentativeVectors(vector1, vector2):
    freeVector1 = getFreeFromRepresentative(vector1)
    freeVector2 = getFreeFromRepresentative(vector2)
    return addFreeVectors(freeVector1, freeVector2)

# Function that calculates the difference of two representative vectors
# Pay attention, because the result will be the free vector corresponding to
# the input
# @return a tuple which represents the resulted free vector
def substractRepresentativeVectors(vector1, vector2):
    freeVector1 = getFreeFromRepresentative(vector1)
    freeVector2 = getFreeFromRepresentative(vector2)
    return substractFreeVectors(freeVector1, freeVector2)

# Simple function which calculates the length of a free vector, using the
# standard formula, known since highscool
# @return a float which represents the length of the vector
def freeVectorLength(vector):
    xSquare = vector[0] ** 2
    ySquare = vector[1] ** 2
    return sqrt(xSquare + ySquare)

# Function that compares 2 free vectors by their lengths
# @return -> a number bigger than 0 if the first vector is longer than the first
#         -> 0 if they have the same length
#         -> a number smaller than 0 otherwise
def compareFreeVectors(vector1, vector2):
    length1 = freeVectorLength(vector1)
    length2 = freeVectorLength(vector2)
    return length1 - length2

# Function that verify if some free vectors can create a polygon
# For this, we will use the polygon property, which implies that the
# sum of all vectors (sides) is equal to null vector (0)
# @return a boolean, True if we can form a polygon, False otherwise
def canBePolygon(freeVectors):
    # we cannot have a polygon with less than 3 sides
    if len(freeVectors) < 3:
        return False
    # compute the sum of the vectors
    result = freeVectors[0]
    for vector in freeVectors[1:]:
        result = addFreeVectors(vector, result)
    # if the resulted vector is 0i + 0j, then we can create a polygon
    if result == (0, 0):
        return True
    # otherwise, there does not exists such a polygon
    else:
        return False

# given the free vectors and knowing that we can perform an polygon
# with them, we will generate a "random" polygon with those vectors,
# by a certain rule; the polygon isn't unique (known fact <--> proprerty)
# therefore we obtain just one posibility of INFINITE ones
# @return a list of representative vectors of a polygon, correlated to
# the free vectors given
def pointsOfSomePolygon(freeVectors):
    # create a list with some represantative vectors starting from the
    # free vectors
    representativeVectors = []
    for freeVector in freeVectors:
        #find a random representative vector for each free vector
        representativeVector = getRepresentativeFromFree(freeVector)
        representativeVectors.append(representativeVector)
    # now, using translation, we will translate all the obtained vectors by this
    # following rule:
    # Step 1: translate the first vector's starting point in origin
    # NOTE: we are talking only about represenative vectors; we call them from
    # now on just vectors to keep it simple and short
    #
    # @return a list of representative vectors; those vectors are concatenated,
    # which implies that we have obtained a polygon
    firstVector = representativeVectors[0]
    startingPoint = firstVector[0]
    xStarting = startingPoint[0]
    yStarting = startingPoint[1]
    representativeVectors[0] = translateVector(
        firstVector, -xStarting, -yStarting)

    # Step 2: we translate the rest of the vectors by the same procedure, only
    # difference being that we translate with the ending point of the previous
    # vector; example: for vector on position 2, the starting point will be the
    # same with de ending point of vector on position 1, and so on
    for i in range(1, len(representativeVectors)):
        previousVector = representativeVectors[i - 1]
        currentVector = representativeVectors[i]
        #ending is specific to previous vector
        endingPoint = previousVector[1]
        xEnding = endingPoint[0]
        yEnding = endingPoint[1]
        #starting is specific to current vector
        startingPoint = currentVector[0]
        xStarting = startingPoint[0]
        yStarting = startingPoint[1]
        representativeVectors[i] = translateVector(
            currentVector, xEnding - xStarting, yEnding - yStarting)
    return representativeVectors

# This is a function which calculates the perp dot product between two
# free vectors; it is somenthing different from simple dot product, but is
# very useful for finding if a polygon is convex or not
# If you are interested in more details about this special product and its
# application, use the following link to this book's pdf:
# http://cas.xav.free.fr/Graphics%20Gems%204%20-%20Paul%20S.%20Heckbert.pdf
#
# @return the perp dot product
def getPerpDotProduct(vector1, vector2):
    a1 = vector1[0]
    b1 = vector1[1]
    a2 = vector2[0]
    b2 = vector2[1]
    result = a1 * b2 - a2 * b1
    return result

# This special function uses the perp dot product formula to find if the polygon
# is convex or concave; we take every two adjacent free vectors and calculate
# the perp dot product of them; then, we study the evolution of signature for
# each pair; If there exists a pair whose perp dot product's signature is
# different from the other pairs, then the polygon is concave; otherwise, it is
# convex. The problem can also be studied in depth using the book at the
# link given at getPerpDotProduct function
# @return True if the polygon is convex, False otherwise
def isConvex(polygon):
    # this represents the orientation(a.k.a the sign) for each perp dot product
    orientation = 0
    for i in range(0, len(polygon)):
        # there is a special case, meaning that the last vector is adjacent with
        # the first one, the polygon assuring the cycle
        if i == len(polygon) - 1:
            nextFreeVector = getFreeFromRepresentative(polygon[i])
            currentFreeVector = getFreeFromRepresentative(
                polygon[len(polygon) - 1])
            perpDotProduct = getPerpDotProduct(
                currentFreeVector, nextFreeVector)
            # there we "initialize" the orientation
            # in future, if orientation changes, even for a single pair, then
            # polygon is not convex
            if perpDotProduct > 0:
                orientation = 1
            elif perpDotProduct == 0:
                orientation = 0
            else:
                orientation = -1
        else:
            nextFreeVector = getFreeFromRepresentative(polygon[i])
            currentFreeVector = getFreeFromRepresentative(polygon[i + 1])
            perpDotProduct = getPerpDotProduct(
                currentFreeVector, nextFreeVector)
            # these three conditions verify if the orientation doesn't change
            if perpDotProduct > 0 and orientation <= 0:
                return False
            elif perpDotProduct == 0 and orientation != 0:
                return False
            elif perpDotProduct < 0 and orientation >= 0:
                return False
        # if we reach this statement, then we are sure that the our polygon is
        # convex
        return True
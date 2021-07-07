import myFunctions

# the free vector is represented by a tuple of 2 elements, one is the coordinate
# for i versor, and the other one is for j versor
freeVector = (3, 2)

# An representative vector is represented as a list with 2 elements, 2 tuples
# more exactly, which represents the starting, respective the ending point of
# the vector; each tuple contains 2 elements, representing the coordinates of
# the given points
representativeVector = [(2, 4), (7, -2)]

# test our print function with freeVector as a parameter
# pay attention: we also use the free to representative "conversion" in this
# step, to obtain a random representative vector. Therefore,  there is no need
# to test again this thing
myFunctions.printVectors(freeVector)

# test the representative to free vector "conversion", this time using the
# representativeVector as a parameter
# Pay attention: we also use the print function to see the changes, but this
# time we'll obtain a NEW REPRESENTATIVE VECTOR, randomly determined
print("--------------------------------------------")
print("Representative vector is:" + str(representativeVector))
resultedFreeVector = myFunctions.getFreeFromRepresentative(representativeVector)
myFunctions.printVectors(resultedFreeVector)

# test the translate function of a representative vector
print("--------------------------------------------")
result = myFunctions.translateVector(representativeVector, 2, 3)
print("Translated vector is:" + str(result))

# test the add operation between two free vectors
print("--------------------------------------------")
print("Checking sum for 3i - j and 2i + 7j")
freeVector1 = (3, -1)
freeVector2 = (2, 7)
resultedFreeVector = myFunctions.addFreeVectors(freeVector1, freeVector2)
myFunctions.printVectors(resultedFreeVector)

# test the substracting operation between two free vectors
print("--------------------------------------------")
print("Checking substraction for the same previous two free vectors: ")
resultedFreeVector = myFunctions.substractFreeVectors(freeVector1, freeVector2)
myFunctions.printVectors(resultedFreeVector)

# test the add operation between two representative vectors
print("--------------------------------------------")
print("Checking sum for  AB and CD, where A(2,6), B(3,5) and C(-2,7), D(4,-5)")
representativeVector1 = [(2, 6), (3, 5)]
representativVector2 = [(-2, 7), (4, -5)]
resultedFreeVector = myFunctions.addRepresentativeVectors\
    (representativeVector1,representativVector2)
myFunctions.printVectors(resultedFreeVector)


# test the substracting operation between two representative vectors
print("--------------------------------------------")
print("Checking substraction for the same previous"
      " two representative vectors: ")
resultedFreeVector = myFunctions.substractRepresentativeVectors\
    (representativeVector1, representativVector2)
myFunctions.printVectors(resultedFreeVector)

# test the length of a free vector
print("--------------------------------------------")
print("Length for free vector 2i + 3j is: ", end = "")
length = myFunctions.freeVectorLength(freeVector)
print(length)

# test the comaprision of two free vectors, by their lebgths
print("--------------------------------------------")
print("Comparision between free vetcors (3, -1) and (2, 7)")
result = myFunctions.compareFreeVectors(freeVector1, freeVector2)
print("The length difference is: " + str(result), end = ", ")
if result == 0:
    print("Same length")
elif result > 0:
    print("First one is longer than the second")
else:
    print("Second one is longer than the first")

#
# There starts the principal part of the exercise
#
# as a test for checking polygon and convexity, we take 5 free vectors
def main():
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    print("--------------------------------------------")
    # modfiy this to test another values
    # First input is not convex, even is a polygon
    # The second one is a convex polygon
    # Comment and uncomment each one to see it working, but not simultaneously
    #freeVectors = [(-1, 1), (0, 1), (3, -3), (2, -1), (-4, 2)]
    freeVectors = [(1, -1), (-1, 1), (1, 1), (-1, -1)]
    print("The vectors can form a polygon: ", end = "")
    posibility = myFunctions.canBePolygon(freeVectors)
    print(posibility)
    # Posibility is used t find out if our free vectors are able to form a
    # polygon or not; if they are, then we will construct one
    if posibility:
        polygonVectors = myFunctions.pointsOfSomePolygon(freeVectors)
        print("Polgyon written with representative vectors is: ", end = "")
        print(polygonVectors)
        print("Notice that beggining of first vector matches the ending of last"
              "vector, so we have obtained a closed line, so, a polygon")
        print("The vertices of the poygon are: ", end = "")
        polygonVertices = []
        for vector in polygonVectors:
            polygonVertices.append(vector[0])
        print(polygonVertices)

        # There we test if the obtained polygon is convex or not
        print("Convexity of the polygon: ", end = "")
        print(myFunctions.isConvex(polygonVectors))

# Keep it simple, keep it in a function; we don't want to make something wrong
# to the previous code; store it in a function
main()


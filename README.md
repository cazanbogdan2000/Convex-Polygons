# Convex-Polygons
  A Python program that finds out if a polygon is convex or not.
We consider a polygon to be a "cluster" of many oriented vectors.
In order to find if the polygon is convex, firstly we have to see
if we can form a polygon with our given vectors (remember that vectors
can be translated), so, it is necessary that the sum of those vectors to
be equal to 0. After we decide if we have a polygon, next step is to see
if that polygon could be convex (no vectors intersected). We'll use the
orthogonal complement (also met as perp product). To get an idea about
mathematical principles behind, visit 
https://www.math.ucla.edu/~josephbreen/Understanding_the_Dot_Product_and_the_Cross_Product.pdf

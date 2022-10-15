# Question: Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, 
# return the maximum number of points that lie on the same straight line.

# Example 1 Input: points = [[1,1],[2,2],[3,3]]
# Output: 3

# Example 2 Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
# Output: 4

from math import inf

class Solution:
    # This function takes 2 points as input, and return a tuples (xk,yk,m) i.e x-intercept, y-intercept, slope of the line formed by the 2 points.
    def getLine(self, p1, p2):
        # Repr of a Line by (xk, yk) - axis intercepts(Destructuring the Points p1, p2) 
        x1,y1 = p1
        x2,y2 = p2
        
        if x1==x2:
            return (x1, inf)
        if y1==y2:
            return (inf, y1)
        
        m = (y2-y1)/(x2-x1)
        xk = round(x2 - y2/m, 8)
        yk = round(y2 - m*x2, 8)
        
        return (xk,yk, m)
    
    # Main 
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 1:
            return 1
        
        # This dictionary stores different lines[denoted via. (xk, yk, m)] as keys
        # The value corresponding to each line will be [<num of points on the line>, <the index of the first point from List[] to be noted in this line>]
        freq = {}
        
        # Iterate over every pair of points 
        for i in range(len(points)-1):
            for j in range(i+1, len(points)):

                line = self.getLine(points[i], points[j])
                
                # If this 'line' is noted for the first time
                if line not in freq:
                    freq[line] = [2, i]
                
                # If the line is already present, just increase the num. of points by 1.
                elif line in freq and freq[line][1] == i:
                    freq[line][0] += 1
                    
        # max(freq.values()) will return the line with maximum '<num of points on the line>'
        return max(freq.values())[0]
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            for value in row:
                if value == target:
                    return True
                
        return False

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:
            if target >= row[0] and target <= row[-1]:
                for value in row:
                    if value == target:
                        return True
                
        return False
        

"""
Farjad/Manuel's solution
"""
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix==None or len(matrix)<1 or len(matrix[0])<1:
            return False
        row = 0
        column = len(matrix[0]) -1 
        while row < len(matrix) and column >=0:
            if matrix[row][column] == target:
                return True
            elif matrix[row][column] < target:
                row += 1
            else:
                column -= 1
        return False

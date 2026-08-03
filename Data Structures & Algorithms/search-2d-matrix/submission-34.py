class Solution:

    def binary_search_col(self, target, row, l, r):
        
        m = l + (r - l) // 2
        print("lrm", l, r, m)
        print("in col", row)
        if l > r:
            return False

        if row[m] == target:
            return True
        elif row[m] < target:
            return self.binary_search_col(target, row, m+1, r)
        return self.binary_search_col(target, row, l, m-1)
    
    def binary_search_row(self, matrix, target, u, d):

        rs = u + (d-u) // 2
        print(u, d, "rs", rs)
        if u > d:
            return False


                
        print("first pass", matrix[rs][-1], matrix[rs][0])
        if matrix[rs][-1] >= target and matrix[rs][0] <= target or len(matrix) == 1 :
            return self.binary_search_col(target,matrix[rs], 0, len(matrix[0])-1)
        elif matrix[rs][-1] < target:
            return self.binary_search_row(matrix, target, rs+1, d)
        
        return self.binary_search_row(matrix, target, u, rs-1)

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        return self.binary_search_row(matrix, target, 0, len(matrix)-1)



        
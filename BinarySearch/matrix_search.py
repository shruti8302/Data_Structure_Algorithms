class MatrixSearch:
    """
    A class to solve the problem of searching for an element in a row-wise and column-wise sorted matrix.
    """

    def matSearch(self, mat, x):
        """
        Searches for an element `x` in a row-wise and column-wise sorted matrix `mat`.

        Args:
            mat (List[List[int]]): A 2D matrix where each row and column is sorted in increasing order.
            x (int): The element to search for in the matrix.

        Returns:
            bool: True if the element is found, False otherwise.
        """
        # Get the dimensions of the matrix
        n = len(mat)      # Number of rows
        m = len(mat[0])   # Number of columns
        
        # Start from the top-right corner of the matrix
        i, j = 0, m - 1
        
        # Traverse the matrix
        while i >= 0 and i < n and j >= 0 and j < m:
            if mat[i][j] == x:
                return True  # Element found
            elif mat[i][j] > x:
                j -= 1       # Move left in the current row
            else:
                i += 1       # Move down to the next row
        
        return False  # Element not found


# Example usage
if __name__ == "__main__":
    # Input matrix
    mat = [
        [3, 30, 38],
        [20, 52, 54],
        [35, 60, 69]
    ]
    x = 62  # Element to search for
    
    # Create an instance of the MatrixSearch class
    solver = MatrixSearch()
    
    # Call the matSearch function
    result = solver.matSearch(mat, x)
    
    # Print the result
    print(result)  # Output: False
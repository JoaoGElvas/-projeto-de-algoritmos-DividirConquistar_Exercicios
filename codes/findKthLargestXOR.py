from typing import List
import heapq

class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        m, n = len(matrix), len(matrix[0])
        xor_matrix = [[0] * n for _ in range(m)]
        values = []

        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    xor_matrix[i][j] = matrix[i][j]
                elif i == 0:
                    xor_matrix[i][j] = xor_matrix[i][j - 1] ^ matrix[i][j]
                elif j == 0:
                    xor_matrix[i][j] = xor_matrix[i - 1][j] ^ matrix[i][j]
                else:
                    xor_matrix[i][j] = xor_matrix[i - 1][j] ^ xor_matrix[i][j - 1] ^ xor_matrix[i - 1][j - 1] ^ matrix[i][j]

                if len(values) < k:
                    heapq.heappush(values, xor_matrix[i][j])
                else:
                    if xor_matrix[i][j] > values[0]:
                        heapq.heappop(values)
                        heapq.heappush(values, xor_matrix[i][j])

        return values[0]

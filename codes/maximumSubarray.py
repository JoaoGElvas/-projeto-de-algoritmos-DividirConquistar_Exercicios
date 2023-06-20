from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]  # Inicializa a soma atual com o primeiro elemento
        max_sum = nums[0]  # Inicializa a soma máxima com o primeiro element
        
        for i in range(1, len(nums)):
            # Atualiza a soma atual, adicionando o elemento atual ou iniciando um novo subarray
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Atualiza a soma máxima quando a soma atual for maior
            max_sum = max(max_sum, current_sum)
        
        return max_sum

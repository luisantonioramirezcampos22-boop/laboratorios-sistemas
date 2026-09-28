from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        # 1. Buscar el primer índice donde nums[i] < nums[i+1]
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # 2. Si existe, buscar un número mayor que nums[i]
        if i >= 0:
            j = len(nums) - 1
            while nums[j] <= nums[i]:
                j -= 1

            # Intercambiar
            nums[i], nums[j] = nums[j], nums[i]

        # 3. Invertir la parte derecha del arreglo
        izquierda = i + 1
        derecha = len(nums) - 1

        while izquierda < derecha:
            nums[izquierda], nums[derecha] = nums[derecha], nums[izquierda]
            izquierda += 1
            derecha -= 1
            
# Pruebas
sol = Solution()

caso1 = [1, 2, 3]
sol.nextPermutation(caso1)
print(caso1)

caso2 = [3, 2, 1]
sol.nextPermutation(caso2)
print(caso2)

caso3 = [1, 1, 5]
sol.nextPermutation(caso3)
print(caso3)

# Casos ocultos
caso4 = [1, 3, 2]
sol.nextPermutation(caso4)
print(caso4)

caso5 = [2, 3, 1]
sol.nextPermutation(caso5)
print(caso5)

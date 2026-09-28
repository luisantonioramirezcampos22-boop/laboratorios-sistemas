from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        # Buscar la primera posición
        def buscar_primera():
            izquierda = 0
            derecha = len(nums) - 1
            resultado = -1

            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2

                if nums[medio] == target:
                    resultado = medio
                    derecha = medio - 1
                elif nums[medio] < target:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1

            return resultado

        # Buscar la última posición
        def buscar_ultima():
            izquierda = 0
            derecha = len(nums) - 1
            resultado = -1

            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2

                if nums[medio] == target:
                    resultado = medio
                    izquierda = medio + 1
                elif nums[medio] < target:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1

            return resultado

        return [buscar_primera(), buscar_ultima()]
        
# Pruebas
sol = Solution()

print(sol.searchRange([5,7,7,8,8,10], 8))
print(sol.searchRange([5,7,7,8,8,10], 6))
print(sol.searchRange([], 0))

# Casos ocultos
print(sol.searchRange([2,2], 2))
print(sol.searchRange([3,3,3], 3))

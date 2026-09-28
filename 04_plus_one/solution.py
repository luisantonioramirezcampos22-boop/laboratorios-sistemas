from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Recorrer el arreglo de derecha a izquierda
        for i in range(len(digits) - 1, -1, -1):

            # Si el dígito es menor que 9, solo se incrementa
            if digits[i] < 9:
                digits[i] += 1
                return digits

            # Si es 9, se convierte en 0 y continúa el acarreo
            digits[i] = 0

        # Si todos eran 9, se agrega un 1 al inicio
        return [1] + digits
        
# Pruebas
sol = Solution()

print(sol.plusOne([1, 2, 3]))     # [1, 2, 4]
print(sol.plusOne([4, 3, 2, 1]))  # [4, 3, 2, 2]
print(sol.plusOne([9]))           # [1, 0]

# Casos ocultos
print(sol.plusOne([9, 9, 9]))     # [1, 0, 0, 0]
print(sol.plusOne([8, 9, 9, 9]))  # [9, 0, 0, 0]

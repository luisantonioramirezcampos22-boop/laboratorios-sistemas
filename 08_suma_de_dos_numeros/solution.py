from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Diccionario para almacenar el número visto y su índice
        valores_vistos = {}
        
        # Recorremos el arreglo obteniendo el índice y el número
        for indice, num in enumerate(nums):
            # Calculamos el complemento requerido para alcanzar el target
            complemento = target - num
            
            # Si el complemento ya existe en nuestro diccionario, encontramos la solución
            if complemento in valores_vistos:
                return [valores_vistos[complemento], indice]
            
            # Si no existe, guardamos el número actual con su índice
            valores_vistos[num] = indice

# --- Pruebas Locales ---
solucion = Solution()

# Ejemplo 1
print("Ejemplo 1:", solucion.twoSum([2, 7, 11, 15], 9))  

# Ejemplo 2
print("Ejemplo 2:", solucion.twoSum([3, 2, 4], 6)) 

# Ejemplo 3
print("Ejemplo 3:", solucion.twoSum([3, 3], 6))     

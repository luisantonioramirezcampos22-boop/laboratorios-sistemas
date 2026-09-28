from typing import List

class Solution:
    def contarElementosUnicos(self, nums: List[int]) -> int:
        frecuencias = {}
        
        # 1. Iterar y llenar el diccionario con las frecuencias
        for numero in nums:
            if numero in frecuencias:
                frecuencias[numero] += 1
            else:
                frecuencias[numero] = 1
                
        # 2. Desafío Extra: Encontrar el número que más veces se repitió
        if frecuencias:
            max_repeticiones = -1
            numero_mas_repetido = None
            
            for numero, cantidad in frecuencias.items():
                if cantidad > max_repeticiones:
                    max_repeticiones = cantidad
                    numero_mas_repetido = numero
            
            print(f"Número más repetido: {numero_mas_repetido} (Aparece {max_repeticiones} veces)")
        else:
            print("Arreglo vacío, no hay número más repetido.")

        # 3. El tamaño del diccionario representa la cantidad de números únicos
        return len(frecuencias)

# Pruebas de los Casos
sol = Solution()

print("Ejecución de Pruebas")
# Ejemplo 3
print("Cantidad de únicos:", sol.contarElementosUnicos([5, 5, 2, 8, 2, 5]))  
# Salida esperada del print extra: Número más repetido: 5 (Aparece 3 veces)
# Salida esperada del return: 3

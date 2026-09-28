class Solution:
    def romanToInt(self, s: str) -> int:
        # Diccionario con el valor de cada número romano
        valores = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0

        # Recorrer la cadena
        for i in range(len(s)):
            # Si existe un siguiente símbolo y es mayor, se resta
            if i < len(s) - 1 and valores[s[i]] < valores[s[i + 1]]:
                total -= valores[s[i]]
            else:
                # En cualquier otro caso se suma
                total += valores[s[i]]

        return total
        
# Pruebas
sol = Solution()

print("III ->", sol.romanToInt("III"))
print("LVIII ->", sol.romanToInt("LVIII"))
print("MCMXCIV ->", sol.romanToInt("MCMXCIV"))
print("IV ->", sol.romanToInt("IV"))
print("IX ->", sol.romanToInt("IX"))
print("MMMCMXCIX ->", sol.romanToInt("MMMCMXCIX"))

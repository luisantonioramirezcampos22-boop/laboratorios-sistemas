class Solution:
    def isPalindrome(self, x: int) -> bool:

        # Los números negativos no son palíndromos
        if x < 0:
            return False

        # Si termina en 0 y no es el número 0, no es palíndromo
        if x != 0 and x % 10 == 0:
            return False

        numero_revertido = 0

        # Revertir solo la mitad del número
        while x > numero_revertido:
            digito = x % 10
            numero_revertido = numero_revertido * 10 + digito
            x = x // 10

        # Para números con cantidad par de dígitos
        # o impar (ignorando el dígito central)
        return x == numero_revertido or x == numero_revertido // 10
        
# Pruebas
sol = Solution()

print(sol.isPalindrome(121))
print(sol.isPalindrome(-121))
print(sol.isPalindrome(10))

# Casos ocultos
print(sol.isPalindrome(0))
print(sol.isPalindrome(12321))
print(sol.isPalindrome(1000021))

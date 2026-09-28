from typing import Optional

# Definición del nodo para la lista simplemente enlazada
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # -------------------------------------------------------------
    # Opción 1: Enfoque Iterativo (Recomendado / Estándar)
    # Complejidad Tiempo: O(n) | Espacio: O(1)
    # -------------------------------------------------------------
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  # Guardamos referencia al siguiente nodo
            curr.next = prev       # Invertimos el puntero del nodo actual
            prev = curr            # Desplazamos 'prev' un paso adelante
            curr = next_temp       # Desplazamos 'curr' un paso adelante
            
        return prev  # 'prev' se convierte en la nueva cabeza

    # -------------------------------------------------------------
    # Opción 2: Enfoque Recursivo (Desafío Extra)
    # Complejidad Tiempo: O(n) | Espacio: O(n) por la pila de llamadas
    # -------------------------------------------------------------
    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Caso base: si la lista está vacía o solo tiene un nodo
        if not head or not head.next:
            return head
        
        # Llamada recursiva para procesar el resto de la lista
        new_head = self.reverseListRecursive(head.next)
        
        # Invertimos la relación entre el nodo siguiente y el actual
        head.next.next = head
        head.next = None
        
        return new_head


# --- Funciones Auxiliares para Pruebas Locales ---

def build_linked_list(arr: list) -> Optional[ListNode]:
    """Crea una lista enlazada a partir de una lista de Python."""
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_linked_list(head: Optional[ListNode]) -> list:
    """Convierte la lista enlazada a una lista de Python para visualizarla."""
    result = []
    curr = head
    while curr:
        result.append(curr.val)
        curr = curr.next
    return result


# --- Pruebas de la Ejecución ---
if __name__ == "__main__":
    sol = Solution()
    
    # Ejemplo 1: [1, 2, 3, 4, 5] -> Salida esperada: [5, 4, 3, 2, 1]
    list1 = build_linked_list([1, 2, 3, 4, 5])
    reversed1 = sol.reverseList(list1)
    print("Ejemplo 1 (Iterativo):", print_linked_list(reversed1))

    # Ejemplo 2: [1, 2] -> Salida esperada: [2, 1]
    list2 = build_linked_list([1, 2])
    reversed2 = sol.reverseListRecursive(list2)  # Probando versión recursiva
    print("Ejemplo 2 (Recursivo):", print_linked_list(reversed2))

    # Ejemplo 3: [] -> Salida esperada: []
    list3 = build_linked_list([])
    reversed3 = sol.reverseList(list3)
    print("Ejemplo 3 (Lista Vacía):", print_linked_list(reversed3))
  

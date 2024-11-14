from metodo_burbuja import bubble_sort
from metodo_insercion import insertion_sort
from metodo_insbin import bin_insertion
from metodo_shell import Shell
from metodo_quick import Quick
from metodo_heap import construir_monticulo
from metodo_radix import Radix

def menu():
    print("\nMétodo de ordenamientos"
          "\n1. Método de Burbuja"
          "\n2. Método de Inserción"
          "\n3. Método de Inserción binaria"
          "\n4. Método de Shell"
          "\n5. Método de Quick"
          "\n6. Método de Heap"
          "\n7. Método de Radix"
          "\n8. Salir del programa"
          "\n")

def pedir_lista():
    lista = input("Ingrese los números a ordenar (separados por comas): ")
    return [int(x.strip()) for x in lista.split(",")]

def main():
    while True:
        menu()
        opcion = input("Seleccione una de las opciones: ")

        if opcion == '1':
            numeros = pedir_lista()
            resultado = bubble_sort(numeros)
            print("Lista ordenada por el método de burbuja:", resultado)
        elif opcion == '2':
            numeros = pedir_lista()
            resultado = insertion_sort(numeros)
            print("Lista ordenada por el método de inserción:", resultado)
        elif opcion == '3':
            numeros = pedir_lista()
            resultado = bin_insertion(numeros)
            print("Lista ordenada por el método de inserción binaria:", resultado)
        elif opcion == '4':
            numeros = pedir_lista()
            shell = Shell()
            shell.ordenamientoDeShell(numeros)
            print("Lista ordenada con el método de Shell", numeros)
        elif opcion == '5':
            numeros = pedir_lista()
            quick = Quick()
            quick.ordenamientoRapido(numeros)
        elif opcion == '6':
            numeros = pedir_lista()
            resultado = construir_monticulo(numeros)
            print("Lista ordenada por el método de Heap:", resultado)
        elif opcion == '7':
            numeros = pedir_lista()
            radix = Radix()
            radix.radix_sort(numeros)
        elif opcion == '8':
            break
        else:
            print("La opción es incorrecta, intente de nuevo con las opciones disponibles.")


if __name__ == "__main__":
    main()
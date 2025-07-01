import sumar
import resta
import multiplicacion
import dividir
import suma_avanzada
import resta_avanzada
import multiplicacion_avanzada

def mostrar_menu():
    print("\n--- Calculadora Open Source ---")
    print("1. Sumar 2 números")
    print("2. Restar 2 números")
    print("3. Multiplicar 2 números")
    print("4. Dividir 2 números")
    print("5. Sumar varios números (avanzada)")
    print("6. Restar varios números (avanzada)")
    print("7. Multiplicar varios números (avanzada)")
    print("8. Salir")
    print("-----------------------------")

def obtener_numeros(cantidad):
    numeros = []
    for i in range(cantidad):
        while True:
            try:
                num = float(input(f"Ingrese el número {i+1}: "))
                numeros.append(num)
                break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
    return numeros

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nums = obtener_numeros(2)
            if nums:
                resultado = sumar.sumar(nums[0], nums[1])
                print(f"El resultado de la suma es: {resultado}")
        elif opcion == '2':
            nums = obtener_numeros(2)
            if nums:
                resultado = resta.restar(nums[0], nums[1])
                print(f"El resultado de la resta es: {resultado}")
        elif opcion == '3':
            nums = obtener_numeros(2)
            if nums:
                resultado = multiplicacion.multiplicar(nums[0], nums[1])
                print(f"El resultado de la multiplicación es: {resultado}")
        elif opcion == '4':
            nums = obtener_numeros(2)
            if nums:
                resultado = dividir.dividir(nums[0], nums[1])
                print(f"El resultado de la división es: {resultado}")
        elif opcion == '5':
            while True:
                try:
                    cantidad = int(input("¿Cuántos números desea sumar? "))
                    if cantidad <= 0:
                        print("Por favor, ingrese un número positivo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            nums = obtener_numeros(cantidad)
            if nums:
                resultado = suma_avanzada.suma_n_numeros(*nums)
                print(f"El resultado de la suma avanzada es: {resultado}")
        elif opcion == '6':
            while True:
                try:
                    cantidad = int(input("¿Cuántos números desea restar? "))
                    if cantidad <= 0:
                        print("Por favor, ingrese un número positivo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            nums = obtener_numeros(cantidad)
            if nums:
                resultado = resta_avanzada.resta_n_numeros(*nums)
                print(f"El resultado de la resta avanzada es: {resultado}")
        elif opcion == '7':
            while True:
                try:
                    cantidad = int(input("¿Cuántos números desea multiplicar? "))
                    if cantidad <= 0:
                        print("Por favor, ingrese un número positivo.")
                        continue
                    break
                except ValueError:
                    print("Entrada inválida. Por favor, ingrese un número entero.")
            nums = obtener_numeros(cantidad)
            if nums:
                resultado = multiplicacion_avanzada.multiplica_n_numeros(*nums)
                print(f"El resultado de la multiplicacion avanzada es: {resultado}")
        elif opcion == '8':
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción inválida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()
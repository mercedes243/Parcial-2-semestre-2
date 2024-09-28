def promedio (a, b, c):
    return (a + b + c) / 3

num1 = int(input("Ingrese un número entero:"))
num2 = int(input("Ingrese un número entero:"))
num3 = int(input("Ingrese un número entero:"))

resultado = promedio(num1, num2, num3)
print(f"El promedio de los tres números es:{resultado}")

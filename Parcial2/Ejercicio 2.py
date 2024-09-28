def calcule_supeficie(lado1, lado2):
     return lado1 * lado2

def main():
    print("Rectángulo 1:")
    lado1_rect1 = float(input("Ingrese el valor del primer lado:"))
    lado2_rect2 = float(input("Ingresa el valor del segundo lado:"))

    print("\nRectángulo 2:")
    lado1_rect1 = float(input("Ingrese el valor del primer lado:"))
    lado2_rect2 = float(input("Ingresa el valor del segundo lado:"))
    
    superficie1 = calcule_supeficie(lado1_rect1, lado2_rect2)
    superficie2 = calcule_supeficie(lado1_rect1, lado2_rect2)
    
    print(f"\nSuperficie del rectángulo 1: {superficie1}")
    print(f"\nSuperficie del rectángulo 1: {superficie2}")
    
    if superficie1 > superficie2:
        print("\nEl rectángulo 1 tiene una mayor superficie.")
    elif superficie1 > superficie2:
        print("\nEl rectángulo 2 tiene una mayor superficie.")
    else:
        print("\nAmbos rectángulos tienen la misma superficie.")


if __name__ == "__main__":
    main()

lado1 = float(input("Digite o lado 1 do triângulo:"))
lado2 = float(input("Digite o lado 2 do triângulo:"))
lado3 = float(input("Digite o lado 3 do triângulo:"))

if(lado1 == lado2 and lado2 == lado3 and lado1 == lado3):
    print("O triângulo é equilátero!")
elif(lado1 == lado2 and lado1 != lado3 and lado2 != lado3 or lado1 == lado3 and lado2 != lado1 and lado2 != lado3 or lado2 == lado3 and lado1 != lado2 and lado1 != lado3):
    print("O triângulo é isósceles!")
else:
    print("O triângulo é escaleno!")

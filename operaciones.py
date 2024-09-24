


# Calculadora perimetro y area de un circulo
import math 
print("Calculadora python")
perimetro=float(input("Ingrese el radio del circulo:"))
co= float(input("ingrese el lado uno del triangulo: "))
ca= float(input("Ingrese el lado dos del triangulo: "))
h= math.sqrt(pow(co, 2)*pow(ca, 2))
p= 2*math.pi*perimetro
area= math.pi*pow(perimetro, 2)
print(f"El perimetro del circulo es : {round(p, 2)}m")
print(f"El area del circulo es : {round(area, 2)}m^2")
print(f"La hipotenusa del triangulo es:{round(h, 2)}")


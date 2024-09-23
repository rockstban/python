# Input

#name= input ("What is your name?: ")
#print(f"Ok your name is : {name}")
#age= input("Now How old are you?: ")
#age1 = int(age)
#age1= age1 +1
#print(f"You are {age} years old")
#print(f"But my birthday is today so I am {age1} years old")

# Programa de Fisica
#print("Calculadora de distancia de Física")
#print("-----MRU------")
#velocidad= int(input("¿Cuál es la velocidad?:"))
#tiempo = int(input("¿Cuál es el tiempo?:"))
#distancia = velocidad * tiempo
#print(f" La distancia que recorre es de: {distancia}m") 

# Calculadora de tienda 

print ("  Resturante Lopez   ")
print ( "---- Gracias por preferirnos  ------ " )
tipo = input("Qué producto desea ordenar?: ")
print(f"El precio por unidad de {tipo} es de $14.50")
precio = 14.50
cantidad= int(input("Cuantos productos desea llevar?:"))
costo = precio * cantidad 
iva= (costo*15)/100
total= iva+costo
print ("----- Detalles del pedido ------")
print(f"Usted pidio: {tipo} con la cantidad de {cantidad}{tipo}")
print(f"El costo es de {costo} sin incluir el iva")
print(f"Por lo tanto el costo total es de ${total}")
print("Gracias por su compra, vuelva pronto")


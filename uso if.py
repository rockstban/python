# if when is true or else for something else 

#print("Credit Card")
#age=input("Enter your age: ")
#age=int(age)
#if age >=120 :
#    print("you are dead sorry :( !!")
#elif age >=20 :
#    print("You can have a credit card")
#elif age <=0 :
#    print("you are so dumb!!!!!")
#else:
#    print("You cant take a credit card")


print("----- Tienda/Restaurante López -----")
pizza= input("Si desea una pizza coloque S o de lo contario N: ")
if pizza == "S":
    print("Que el costo por unidad de pizza es de $10.99")
    cp=int(input("Cuantas pizzas quieres:"))
    vp= 10.99
    costo= cp*vp
    iva= float((costo*15)/100)
    total= costo+iva
    print(f"El valor de las pizzas es de ${round(costo, 2)} sin incluir el iva")
    print(f"El valor total es de ${round(total, 2)}")
elif pizza != "S":
    print("Recomendamos ir a un doctor coloque las letras que se solicita")
else :
    print("Pasamos al siguiente alimento, gracias")
    
lasaña= input("Si desea una lasaña coloque S o de lo contario N: ")
if lasaña == "S":
    print("El costo por unidad de lasaña es de $5.99")
    cl=int(input("Cuantas lasañas quieres:"))
    vl= 5.99
    costo2= cl*vl
    iva2= float((costo2*15)/100)
    total2= costo2+iva2
    print(f"El valor de las lasañas es de ${round(costo2, 2)} sin incluir el iva")
    print(f"El valor total es de ${round(total2, 2)}")
elif lasaña != "S":
    print("Recomendamos ir a un doctor coloque las letras que se solicita")
else :
    print("Pasamos al siguiente alimento, gracias") 
#pollo= input("Si desea una pollo coloque S o de lo contario N: ")
#if pizza == "S":
#    print("Que el costo por unidad de pizza es de $10.99")
#    cp=int(input("Cuantas pizzas quieres:"))
#    vp= 10.99
#    costo= cp*vp
#    iva= float((costo*15)/100)
#    total= costo+iva
#    print(f"El valor de las pizzas es de ${round(costo, 2)} sin incluir el iva")
#    print(f"El valor total es de ${round(total, 2)}")
#elif pizza != "S":
#    print("Recomendamos ir a un doctor coloque las letras que se solicita")
#else :
#    print("Pasamos al siguiente alimento, gracias") 
#pinchos= input("Si desea una pinchos coloque S o de lo contario N: ")
#if pizza == "S":
#    print("Que el costo por unidad de pizza es de $10.99")
#    cp=int(input("Cuantas pizzas quieres:"))
#    vp= 10.99
#    costo= cp*vp
#    iva= float((costo*15)/100)
#    total= costo+iva
 #   print(f"El valor de las pizzas es de ${round(costo, 2)} sin incluir el iva")
#    print(f"El valor total es de ${round(total, 2)}")
#elif pizza != "S":
#    print("Recomendamos ir a un doctor coloque las letras que se solicita")
#else :
#    print("Pasamos al siguiente alimento, gracias") 

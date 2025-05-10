nombre = input("Ingrese su nombre completo")
edad_actual = input(" ingrese su edad actual")
dias_vividos = (edad_actual*365)
with open('dias.txt','w') as archivo:
    archivo.write(f"Este es el resultado que quiero guardar.{dias}")
print(f"{dias_vividos}")

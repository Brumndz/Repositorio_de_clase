print("nombre de rango de edad")
edad = int(input("ingrese edad"))
if edad <= 4:
    print("infante")
elif edad <= 10:
    print("niño")
elif edad <= 14:
    print("preadolescente")
elif edad <= 24:
    print("adulto joven")
elif edad <= 40:
    print("adulto intermedio")
elif edad >= 60:
    print("adulto mayor")
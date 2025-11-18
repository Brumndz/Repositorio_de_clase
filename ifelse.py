print("peliculas")
print("genero de peliculas")
print("1.- accion")
print("2.- comedia")
genre = int(input("ingrese su genero de peliculas favorito: "))
age = int(input("ingrese su edad: "))

if age >= 13 and genre == 1:
        print("mira deadpool")
elif age < 13 and genre == 1:
        print("mira regreso al futuro")
elif genre == 2:
        print("mira aterriza como puedas")
else:
        print("explora mas generos")

    


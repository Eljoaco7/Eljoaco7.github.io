for i in range(5):
    vidas = int(input("ingrese un numero de vidas"))
    if vidas >= 5:
        print("Bienvenido jugador... Estas jugando en dificultad FACIL")
    elif 3 <= vidas <= 4:
        print("Bienvenido jugador... Estas jugando en dificultad MEDIA")
    elif vidas <= 2:
        print("Bienvenido jugador... Estas jugando en dificultad DIFICIL")
    else:
        print("No se pudo determinar la dificultad")
    



welcome = """
                        ************************************************************
                        *                                                          *
                        *        Welcome to the Rock, Paper, Scissors Game!        *
                        *                                                          *
                        ************************************************************
"""
print(welcome)


def posibilidad_elemento():
    posibilidades = ["Para Piedra poner PI", "Para Papel poner PA", "Para Tijera poner TI"]
    print("Elementos posibles:")
    print('\n'.join(map(str, posibilidades)))

def hide_players_choice():
    print(f"\n " * 50)

#_____________________________________________________________________________________________________________________
print("Ahora, con el participante numero uno!")
contrincante_1 = input("\nIngrese nombre participante numero 1: ")
print(contrincante_1,"Sera el partincipante numero 1 \n ")

posibilidad_elemento()
while True:
    elemento_1 = input("Elija su elemneto: ").upper()

    if elemento_1 == "pi".upper() or elemento_1 == "pa".upper() or elemento_1 == "ti".upper():
        break
    else:
        print("Elemento Invalido, intente de nuevo con el comando correspondiente ")
        continue

hide_players_choice()

#_____________________________________________________________________________________________________________________
print("Ahora, con el participante numero dos!")
contrincante_2 = input("\nIngrese nombre participante numero 2: ")
print(contrincante_2,"Sera el partincipante numero 2 \n ")

posibilidad_elemento()
while True:
    elemento_2 = input("Elija su elemneto: ").upper()

    if elemento_2 == "pi".upper() or elemento_2 == "pa".upper() or elemento_2 == "ti".upper():
        break
    else:
        print("Elemento Invalido, intente de nuevo con el comando correspondiente ")
        continue



if (elemento_1 == "PA") and (elemento_2 == "PI"):
    print(f"\nGana {contrincante_1}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "PI") and (elemento_2 == "PA"):
    print(f"\nGana {contrincante_2}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "PI") and (elemento_2 == "TI"):
    print(f"\nGana {contrincante_1}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "TI") and (elemento_2 == "PI"):
    print(f"\nGana {contrincante_2}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "TI") and (elemento_2 == "PA"):
    print(f"\nGana {contrincante_1}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "PA") and (elemento_2 == "TI"):
    print(f"\nGana {contrincante_2}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

else:
    print("\nEmpate")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")


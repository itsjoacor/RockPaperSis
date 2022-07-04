
print("Bienvenidos")
print("Este es un juego de Piedra, Papel o Tijera.")

contrincante_1 = input("Ingrese nombre participante numero 1: ")
print(contrincante_1,"Sera el partincipante numero 1 \n ")

posibilidades = ["Para Piedra poner PI", "Para Papel poner PA", "Para Tijera poner TI"]
print("Elementos posibles:")
print('\n'.join(map(str, posibilidades)))

elemento_1 = input("Elija su elemneto:  ").upper()


contrincante_2 = input("\nIngrese nombre participante numero 2: ")
print(contrincante_2,"Sera el partincipante numero 2 \n ")

posibilidades = ["Para Piedra poner PI", "Para Papel poner PA", "Para Tijera poner TI"]
print("Elementos posibles:")
print('\n'.join(map(str, posibilidades)))
elemento_2 = input("Elija su elemento: ").upper()


if (elemento_1 == "PA") and (elemento_2 == "PI"):
    print(f"Gana {contrincante_1}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "PI") and (elemento_2 == "PA"):
    print(f"Gana {contrincante_2}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "PI") and (elemento_2 == "TI"):
    print(f"Gana {contrincante_1}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "TI") and (elemento_2 == "PI"):
    print(f"Gana {contrincante_2}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "TI") and (elemento_2 == "PA"):
    print(f"Gana {contrincante_1}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

elif (elemento_1 == "PA") and (elemento_2 == "TI"):
    print(f"Gana {contrincante_2}")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")

else:
    print("Empate")
    print(f"{contrincante_1} eligió {elemento_1}")
    print(f"{contrincante_2} eligió {elemento_2}")



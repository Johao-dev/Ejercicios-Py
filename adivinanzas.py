
secret_word = "peine"
user_word = input("Ingresa la palabra secreta: ")
contador = 1

while user_word != secret_word:
        print("Esa no es la palabra secreta.")
        user_word = input("Intentalo nuevamente: ")
        contador += 1

        if contador == 3:
            pista = input("¿Quieres una pista?(SI/NO): ").upper()
            if pista == "SI":
                print("Me usas todos los dias...")
                user_word = input("Intentalo nuevamente: ")
            elif pista == "NO":
                print("Bueno xd")
                user_word = input("Intentalo nuevamente: ")
        
        if contador == 6:
             rendir = input("¿Te rindes?(SI/NO):").upper()
             if rendir == "SI":
                  break
             elif rendir == "NO":
                  user_word = input("Intentalo nuevamente: ")

        if contador == 10:
             print("Demasiados intentos :(")
             break

print(secret_word, "Era la palabra secreta.")

def jugar(palabra_adivinar,vidas):
    '''
    Función que permite jugar al ahorcado.

    Input:

        palabra_adivinar -> String
        vidas -> int
    '''
    
    palabra_adivinar = palabra_adivinar.upper()
    palabra_mostrar_lista = list('_' * len(palabra_adivinar))
    print(*palabra_mostrar_lista)
    # Mientras tengamos vidas y palabras por adivinar, se ejecutará este bucle
    while vidas > 0 and '_' in palabra_mostrar_lista:

        # Recogemos la letra del usuario
        letra_usuario = input("Introduzca una letra: ").upper()

        # Comprobamos si queremos salir
        if letra_usuario == "EXIT":
            break
        
        # Compruebo si la letra se encuentra dentro de la palabra
        if letra_usuario in palabra_adivinar:
            print("Has acertado")

            # Me recorro las letras, para encontrar la posición de la letra adivinada
            for pos, letra in enumerate(palabra_adivinar):
                
                # Si coincide, modifico en la lista de caracteres "_", el valor de la letra adivinada en la posición que le corresponde
                if letra == letra_usuario:
                    palabra_mostrar_lista[pos] = letra
                # Si no, no hacemos nada
                else:
                    continue

        # Si no tiene esa letra, ha fallado y por lo tanto pierdes una vida
        else:
            print("Has fallado")
            vidas = vidas - 1
            print("Te quedan",vidas,'vidas')

        # Se muestra la palabra con las letras adivinadas
        print(*palabra_mostrar_lista)
        
    if vidas > 0 and letra_usuario != "EXIT":
        print("Has ganado!! La palabra era", palabra_adivinar)
    else:
        print("Has perdido. La palabra era", palabra_adivinar)
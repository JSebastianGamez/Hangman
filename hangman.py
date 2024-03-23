palabraAdivinar = ''
listaPalabraAdiv = []
listaPalabraMost = []
intentos = 5
letra = ''
run = True

# Logica

## Pedimos la palabra a adivinar
print('AHORCADO')
palabraAdivinar = input('Dime una palabra: ')

## Separamos la palabra en letras
listaPalabraAdiv = list(palabraAdivinar)

for item in listaPalabraAdiv:
    listaPalabraMost.append('_')

while run:
    ## Mostramos la palabra a adivinar
    print(' '.join(listaPalabraMost))

    ## Pedimos una letra
    letra = input('Dame una letra: ')

    ## Limpiar pantalla
    for num in range(100):
        print()

    ## Comprueba si se ha equivocado
    fallo = False

    if letra not in listaPalabraAdiv:
        ## Ha fallado
        fallo = True
        intentos = intentos - 1
        print('Has fallado!!!! Te quedan {intentos} intentos'.format(intentos=intentos))
    else:
        ## Adivinado, sustituimos
        for key, value in enumerate(listaPalabraAdiv):
            if value == letra:
                listaPalabraMost[key] = value

    ## Comprueba si ha terminado la partida
    ### Se le acaban los intentos
    if intentos <= 0:
        run = False
        print('Has perdido, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
    elif listaPalabraAdiv == listaPalabraMost:
        run = False
        print('Has ganado, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))
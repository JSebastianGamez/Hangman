paladv = ''
listpaladv = []
listpalmost = []
intentos = 5
letra = ''
run = True


## asking for a word
print('AHORCADO')
paladv = input('Dime una palabra: ')

## splitting word
listpaladv = list(paladv)

for item in listpaladv:
    listpalmost.append('_')

while run:
    ## showing word to guess
    print(' '.join(listpalmost))

    ## ask for a letter
    letra = input('Dame una letra: ')

    ## clean screen
    for num in range(100):
        print()

    ## checks if failed
    fallo = False

    if letra not in listpaladv:
        ## failed
        fallo = True
        intentos = intentos - 1
        print('Has fallado!!!! Te quedan {intentos} intentos'.format(intentos=intentos))
    else:
        ## guessing the word
        for key, value in enumerate(listpaladv):
            if value == letra:
                listpalmost[key] = value

    ## Checks if game is over
    ### Running out of attempts
    if intentos <= 0:
        run = False
        print('Has perdido, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listpaladv)))
    elif listpaladv == listpalmost:
        run = False
        print('Has ganado, la palabra '
              'era "{palabra}"'.format(palabra=''.join(listaPalabraAdiv)))

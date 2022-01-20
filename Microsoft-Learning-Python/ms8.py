print('Enter player name')
name = input()
print('Spiel fortsetzen?')
eingabe = input()
if eingabe == 'j' or eingabe == 'ja':
    print('Spiel startet, '+ name)
elif eingabe == 'n' or eingabe == 'nein':
    print('Spiel beendet, '+ name)
else:
    print('Falsche Eingabe, '+ name)


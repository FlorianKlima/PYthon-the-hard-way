print("Enter player name")
name = input()
print("Spiel fortsetzen?")
eingabe = input()
if eingabe in ["j", "ja"]:
    print(f"Spiel startet, {name}")
elif eingabe in ["n", "nein"]:
    print(f"Spiel beendet, {name}")
else:
    print(f"Falsche Eingabe, {name}")

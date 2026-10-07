startwert = float(input("Startwert in €: "))
rendite = float(input("Rendite in %: "))
laufzeit = int(input("Laufzeit in Jahren: "))

endwert = startwert * (1 + rendite / 100) ** laufzeit

for jahr in range(1, laufzeit + 1):
    endwert_jahr = startwert * (1 + rendite / 100) ** jahr
    print(f"Jahr {jahr}: {endwert_jahr:.2f}€")
print(f"Endwert: {endwert:.2f}€")
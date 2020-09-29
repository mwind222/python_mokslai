# turime sarasa pasikartojanciu elementu (skaiciu)
skaiciai = [1, 2, 3, 4, 67, 132, 3, 1, 1, -1 , -1, 1.3, 1.3 , 2.2]

# skaiciuojam  kiekvieno saraso elemento pasikartojimus
for elementas in skaiciai:
    pasikartojimai = skaiciai.count(elementas)

    # ismetam pasikartojancius is skaiciai saraso
    # paliekam tik viena pasikartojima
    if pasikartojimai > 1:
        skaiciai.remove(elementas)
    print(elementas, pasikartojimai, sep='\t\t')

print()
print(skaiciai)

# Surusiuojam sarasa. rusiuoja tik int ar float
skaiciai.sort()
print(skaiciai)

# toliau uzduotis surusiuoti pagal pasikartojima..
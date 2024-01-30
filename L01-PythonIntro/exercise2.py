forfattere = ['Ingeborg', 'Andersen', 'Tolkien', 'Frankenstein', 'Dog']

for forf in forfattere:
    print(forf)

forfattere.append('Kat')
for forf in forfattere:
    print(forf)

forfattere.pop(1)
for forf in forfattere:
    print(forf)

length = len(forfattere)
print(length)

forfattere.reverse()
for forf in forfattere:
    print(forf)

books = ['Stealheart', 'Firefight', 'Osmosis', 'Calamity']

books.append('The final empire')
books.append('Twilight saga')
books.append('Harry Potter')
books.append('You can do')

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books[6] = 'The wall of ascension' #update
books[-1] = 'The hero of ages'
books[2] = 'Legions'

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.insert(3, 'Legions: Skindeep' )
books.insert(5, 'Elantris')

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')

books.remove('Stealheart')
books.remove('Legions')

print('idx\t| books')
for i,b in enumerate(books):
    print(f'{i}\t| {b}')
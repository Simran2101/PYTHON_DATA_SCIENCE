from pprint import pprint

movies = {}

# adding a single value
movies['sholay'] = '2 friends fight with a dacoit'
movies['inception'] = 'no summary available'

# adding multiple values
movies.update(
    ironman='man builds a suit that is not iron',
    hulk ='story about a man that is not a hulk',
    batman ='hero dressed as a bat')

movies.pop('sholay')   

# update 1
movies['inception'] = 'dream within dream with recursion logic'

# update 2
movies['batman'] += ' and fights crimes at nights'
pprint(movies)
    
    
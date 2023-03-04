class Movies:
    def __init__(self, pTitle, pGenre, pLanguage, pDirectors, pYear):
        self.title = pTitle
        self._genre = pGenre
        self.language = pLanguage
        self.directors = pDirectors
        self.year = pYear

    def __str__(self):
        return f'Title={self.title}\nGenre={self._genre}\nLanguage={self.language}\n' \
               f'Directors={self.directors}\nYear={self.year}\n'

    @property
    def genre(self):
        return self._genre

    @genre.setter
    def genre(self, value):
        if value in ['Romance', 'Action', 'Drama', 'Thriller', 'Horror']:
            self._genre = value
        else:
            print(f'{value} is an invalid genre\n')

    def recommendMovie(self):
        recommendations = {'Romance': 'First Date', 'Action': 'Mutant',
                           'Drama': 'The Awakening', 'Thriller': 'Mr K',
                           'Horror': 'A walk down Dawson Street'}
        print(f'You may also like the following movie:{recommendations[self._genre]}')

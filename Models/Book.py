from . import warp, unwarp, prolog


class Book(object):
    def __init__(self, Title, Year, Mark, Authors, Genres):
        self.author = Authors
        self.title = unwarp(Title)
        self.year = Year
        self.genres = Genres
        self.mark = Mark

    def Title(self):
        return self.title

    def Year(self):
        return self.year

    def save(self):
        prolog.assertz("book({},{},{})".
                       format(warp(self.title), self.year, self.mark))
        for genre in self.genres:
            print("Add genre")
            prolog.assertz("genre({},{})".format(warp(genre.Name()),
                                                 warp(self.Title())))
        for author in self.author:
            print("Add author")
            prolog.assertz("author({},{},{})".
                           format(warp(author.Name()), warp(author.Surname()),
                                  warp(self.Title())))

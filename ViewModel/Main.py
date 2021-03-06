from PyQt5 import QtWidgets, uic
from . import AddAuthor, AddBook, AddGenre, \
    ListGenre, ListAuthor, ListBook


class MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = uic.loadUi('Views/Main.ui', self)

        self.ui.addAuthorButton.clicked.connect(self.addAuthor)
        self.ui.addBookButton.clicked.connect(self.addBook)
        self.ui.addGenreButton.clicked.connect(self.addGenre)
        self.ui.authorListButton.clicked.connect(self.listAuthor)
        self.ui.genreListButton.clicked.connect(self.listGenre)
        self.ui.bookListButton.clicked.connect(self.listBook)

    def addAuthor(self):
        authorWindow = AddAuthor.AddAuthorWindow()
        authorWindow.show()

    def addBook(self):
        bookWindow = AddBook.AddBookWindow()
        bookWindow.show()

    def addGenre(self):
        genreWindow = AddGenre.AddGenreWindow()
        genreWindow.show()

    def listAuthor(self):
        listWindow = ListAuthor.ListAuthorWindow()
        listWindow.show()

    def listGenre(self):
        listWindow = ListGenre.ListGenreWindow()
        listWindow.show()

    def listBook(self):
        listWindow = ListBook.ListBookWindow()
        listWindow.show()

import sys, random
from PyQt5 import QtCore, QtGui, QtWidgets, uic

form_class = uic.loadUiType("hangman.ui")[0]

# возвращает массив со всеми индексами нахождения буквы
def find_letters(letter, a_string):
    locations = []
    start = 0
    while a_string.find(letter, start, len(a_string)) != -1:
        location = a_string.find(letter, start, len(a_string))
        locations.append(location)
        start = location + 1
    return locations

# заменяет звёздочки на угаданную букву
def replace_letters(string, locations, letter):
    new_string = ""
    for i in range(0, len(string)):
        if i in locations:
            new_string += letter
        else:
            new_string += string[i]
    return new_string

# заменяет русские буквы на тире
def dashes(word):
    letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    new_string = ''
    for i in word:
        if i in letters:
            new_string += "-"
        else:
            new_string += i
    return new_string


class Hangman(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        # обработчики
        self.btn_guess.clicked.connect(self.btn_guess_clicked)
        self.actionExit.triggered.connect(self.menuExit_selected)
        # части человечка
        self.pieces = [self.head, self.body, self.leftarm, self.leftleg,
                       self.rightarm, self.rightleg]
        self.pieces_shown = 0
        # виселица
        self.gallows = [self.line1, self.line2, self.line3, self.line4]
        # получаем список слов
        self.currentword = ""
        f = open("words.txt", 'r')
        self.lines = f.readlines()
        f.close()
        # запуск игры
        self.new_game()

    def new_game(self):
        # выбор слова
        self.guesses.setText("")
        self.currentword = random.choice(self.lines)
        self.currentword = self.currentword.strip()
        # скрываем человечка
        self.pieces_shown = 0
        for i in self.pieces:
            i.setFrameShadow(QtWidgets.QFrame.Plain)
            i.setHidden(True)
        for i in self.gallows:
            i.setFrameShadow(QtWidgets.QFrame.Plain)
        # замена букв на чёрточки
        self.word.setText(dashes(self.currentword))

    def btn_guess_clicked(self):
        guess = str(self.guessBox.text())
        if str(self.guesses.text()) != "":
            self.guesses.setText(str(self.guesses.text()) + ", " + guess)
        else:
            self.guesses.setText(guess)
        # угадываем букву
        if len(guess) == 1:
            if guess in self.currentword:
                locations = find_letters(guess, self.currentword)
                self.word.setText(replace_letters(str(self.word.text()), locations, guess))
                if str(self.word.text()) == self.currentword:
                    self.win()
            else:
                self.wrong()
        # угадываем слово
        else:
            if guess == self.currentword:
                self.win()
            else:
                self.wrong()
        self.guessBox.setText("")

    def win(self):
        # выйгрыш игрока
        QtWidgets.QMessageBox.information(self, "Висельница", "Ты победил!")
        self.new_game()

    def wrong(self):
        # показываем новую часть человечка
        self.pieces_shown += 1
        for i in range(self.pieces_shown):
            self.pieces[i].setHidden(False)
        if self.pieces_shown == len(self.pieces):
            # игрок проиграл
            message = "Ты проиграл. Слово было - " + self.currentword
            QtWidgets.QMessageBox.warning(self, "Висельница", message)
            self.new_game()

    def menuExit_selected(self):
        self.close()


app = QtWidgets.QApplication(sys.argv)
hangman = Hangman()
hangman.show()
app.exec_()

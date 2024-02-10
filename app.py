from PyQt5.uic import *
from PyQt5.QtWidgets import *

app = QApplication([])
f = loadUi("design.ui")
f.show()


def valideNums(n):
    valide = True
    i = 0
    while valide and i < len(str(n)):
        valide = ((int(str(n)[i])%2) == 0)
        i += 1
    return valide


def superpairplus(n):
    d = 2
    valide = True
    while valide and d < n:
        if n % d == 0 and d % 2 != 0:
            valide = False
        else:
            d += 1
    return valide

def lesDiviseurs(n):
    r = ""
    d = 2
    while d < n:
        if n % d == 0:
            r += str(d)+", "
        d += 1
    return r[:-2]

def lesChifre(n):
    r = ""
    for i in range(len(str(n))):
        r += str(n)[i] + ", "
    return r[:-2]

def numImpair(n):
    r = ""
    d = 2
    while r == "" and d < n:
        if n % d == 0 and  d%2 != 0:
            r += str(d)
        d += 1
    return r

def afficher():
    if f.num.text().isdigit():
        n = int(f.num.text())
        if n <= 0:
            QMessageBox.critical(f, "erreur", "svp n > 0")
        elif n % 2 == 0 and valideNums(n) and superpairplus(n):
            f.result.setText(str(n) + " est pair, est formé uniquement par des chiffres pair ("+lesChifre(n)+") et les diviseurs de "+str(n)+" est pairs ("+lesDiviseurs(n)+"), Donc " + str(n) + "est superpair.")
            f.result.setStyleSheet("background-color: #3dd164;color: white;border-radius: 12px;padding-left: 10px;padding-right: 10px;padding-top: 5px;padding-bottom: 5px;")
        else:
            if n % 2 != 0:
                msg = str(n) + " est impair !"
            elif not valideNums(n):
                msg = str(n) + " n'est pas formé uniquement par des chiffres pair ("+lesChifre(n)+") !"
            else:
                msg = "les diviseurs de "+str(n)+" est pairs ("+lesDiviseurs(n)+") pour que "+numImpair(n)+" est impair !"
            f.result.setText(msg)
            f.result.setStyleSheet("background-color: #db431d;color: white;border-radius: 12px;padding-left: 10px;padding-right: 10px;padding-top: 5px;padding-bottom: 5px;")
    else:
        QMessageBox.critical(f, "erreur", "svp 'n' est entier!")

def annuler():
    f.num.setText("")
    f.result.setText("")
    f.result.setStyleSheet("background-color: rgb(255, 255, 255);color: rgb(0, 0, 0);border-radius: 12px;padding-left: 10px;padding-right: 10px;padding-top: 5px;padding-bottom: 5px;")


f.btn.clicked.connect(afficher)
f.reset.clicked.connect(annuler)
app.exec()
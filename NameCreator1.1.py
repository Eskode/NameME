# -*- coding: utf-8 -*-

import os
# import sys
import random
from tkinter import *


# celui qui lit ça a PERDU


# Construction de la matrice de transistion
def build_matrice(file, gender):
    txt = open("Corpus\\" + file)
    for t in txt.readlines():
        line = [t[0], t[2:]]
        if line[0] == gender or line[0] == "x" or gender == "x":
            line[1] = line[1] + "\n"
            for j in range(0, len(line[1]) - 2):
                x = line[1][j]
                y = line[1][j + 1]
                z = line[1][j + 2]
                if j == 0:
                    if ("$$", -1, x + y) not in matrice:
                        matrice["$$", -2, x + y] = 1
                    elif ("$$", -1, x + y) in matrice:
                        matrice["$$", -2, x + y] += 1
                if (x + y, j - 1, z) not in matrice:
                    matrice[x + y, j - 1, z] = 1
                elif (x + y, j - 1, z) in matrice:
                    matrice[x + y, j - 1, z] += 1


# Calcul des probas
def calc_proba():
    global matrice
    matrice2 = {}
    for i in matrice:
        if (i[0], i[1]) not in matrice2:
            matrice2[i[0], i[1]] = [[i[2], matrice[i]]]
        elif (i[0], i[1]) in matrice2:
            matrice2[i[0], i[1]] += [[i[2], matrice[i]]]
    matrice = matrice2


# Création d'un nom
def name_gener():
    nameTot = ""
    rang = 0
    name = "$$"
    while name[-1] != "\n":
        if (name == "$$"):
            prob = matrice[name[-2] + name[-1], len(name) - 4]
            tot = 0
            for i in prob:
                tot += i[1]
                n = random.randint(1, tot)
            tot = 0
            for i in prob:
                tot += i[1]
                if n <= tot:
                    name += i[0]
                    break
        else:
            prob = matrice[name[-2] + name[-1], len(name) - 5]
            tot = 0
            for i in prob:
                tot += i[1]
                n = random.randint(1, tot)
            tot = 0
            for i in prob:
                tot += i[1]
                if n <= tot:
                    name += i[0]
                    break
    return name


# gogogo
def go():
    zone_name1.config(text="")
    zone_name2.config(text="")
    zone_name3.config(text="")
    global matrice
    matrice = {}
    g = genre.get()
    sel = 0
    for i in selection:
        if i[1].get() == 1:
            sel = 1
            build_matrice(i[0], g)
    if sel == 1:
        calc_proba()
        name_liste1 = []
        name_liste2 = []
        name_liste3 = []
        for i in range(0, 27):
            if (i % 3) == 0:
                name_liste1.append(name_gener()[2:-1] + "\n")
            elif (i % 3) == 1:
                name_liste2.append(name_gener()[2:-1] + "\n")
            else:
                name_liste3.append(name_gener()[2:-1] + "\n")
        tmp = u"".join(name_liste1)
        tmp = tmp
        zone_name1.config(text=tmp)
        tmp = u"".join(name_liste2)
        tmp = tmp
        zone_name2.config(text=tmp)
        tmp = u"".join(name_liste3)
        tmp = tmp
        zone_name3.config(text=tmp)
    else:
        zone_name1.config(text="Selectionne au moins un corpus !!\n\n\nHostie d'incompétent ...")


# construction fenetre
def build(liste_files):
    global fenetre
    fenetre = Tk()
    FrameT = Frame(fenetre, borderwidth=2, relief=GROOVE)
    FrameT.pack(side=TOP, padx=40, pady=30)
    FrameL = Frame(FrameT, borderwidth=1, relief=GROOVE)
    FrameL.pack(side=LEFT, padx=10, pady=10)
    FrameR = Frame(FrameT, borderwidth=1, relief=GROOVE)
    FrameR.pack(side=RIGHT, padx=10, pady=10)
    Label(FrameT, text="NAME CREATOR").pack(padx=10, pady=10)
    Label(FrameL, text="Selectionner les corpus").pack(padx=10, pady=10)
    Label(FrameR, text="Options").pack(padx=10, pady=10)
    global l
    l = LabelFrame(fenetre, text="Résultats", padx=20, pady=20)
    l.pack(side=BOTTOM, fill="both", expand="yes")
    global zone_name1
    zone_name1 = Label(l, text="", height=10, anchor=W, justify=LEFT)
    zone_name1.pack(side=RIGHT, fill="both", expand="yes")
    global zone_name2
    zone_name2 = Label(l, text="", height=10, anchor=W, justify=LEFT)
    zone_name2.pack(side=RIGHT, fill="both", expand="yes")
    global zone_name3
    zone_name3 = Label(l, text="", height=10, anchor=W, justify=LEFT)
    zone_name3.pack(side=RIGHT, fill="both", expand="yes")
    Label(l, text="").pack()
    global selection
    selection = []
    for i in liste_files:
        global varSele
        varSele = IntVar()
        bouton = Checkbutton(FrameL, text=i.split('-')[-1][1:-4], variable=varSele)
        bouton.pack()
        selection.append((i, varSele))
    global genre
    genre = StringVar()
    genre.set("x")
    boutonF = Radiobutton(FrameR, text="Homme", variable=genre, value="m")
    boutonM = Radiobutton(FrameR, text="Femme", variable=genre, value="f")
    boutonX = Radiobutton(FrameR, text="???", variable=genre, value="x")
    boutonF.pack()
    boutonM.pack()
    boutonX.pack()
    boutonG = Button(FrameT, text="GO", command=go)
    # boutonC=Button(FrameR, text="Fermer", command=fenetre.destroy)
    boutonG.pack(side="bottom", fill='both', expand=True, padx=20, pady=100)
    # boutonC.pack(side="bottom", fill='both', expand=False, padx=4, pady=4)
    fenetre.mainloop()


# main
def main():
    liste_files = os.listdir("Corpus")
    matrice = {}
    build(liste_files)


##START
main()

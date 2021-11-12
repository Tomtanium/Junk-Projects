#!/usr/bin/env python3

from random import *

player_score = 0
computer_score = 0

def hangedman(hangman):
    graphic = [
    """

        +-------+
        |
        |
        |
        |
        |
    ================
    """
        ,
    """
        +-------+
        |       0
        |
        |
        |
        |
    ================
    """
        ,
    """
        +-------+
        |       0
        |       |
        |
        |
        |
    ================
    """
        ,
    """
        +-------+
        |       0
        |      -|
        |
        |
        |
    ================
    """
        ,
    """
        +-------+
        |       0
        |      -|-
        |
        |
        |
    ================
    """
        ,
    """
        +-------+
        |       0
        |      -|-
        |      /
        |
        |
    ================
    """
        ,
    """
        +-------+
        |       0
        |      -|-
        |      / \\
        |
        |
    ================
    """]

    print(graphic[hangman])
    return

def start():
    print("Let's play a game of GNU/Linux Hangman")
    while game():
        pass
    scores()

def game():
    dictionary = ["gnu","kernel","linux","hurd","tux","penguin","ubuntu","gentoo","fedora","trisquel","parabola"]
    word = choice(dictionary)
    word_length = len(word)

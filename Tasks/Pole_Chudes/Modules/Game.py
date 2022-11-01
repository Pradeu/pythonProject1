import random


def game_start():
    lives = 3
    game_words = open("Words.txt", mode="r")
    game_words = game_words.read().splitlines()
    while lives != 0:
        word_choose = random.choice(game_words)

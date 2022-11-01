import random


def game_start():
    lives = 3
    game_words = open("Modules/Words.txt", mode="r")
    game_words = game_words.read().splitlines()
    while lives != 0:
        word_choose = random.choice(game_words)
        print(word_choose)
        word_cipher = "□□□□□"
        while lives != 0:
            print(f"Загаданное слово: {word_cipher}\n")
            ans_let = input("Введите букву или слово: ")
            ans_pos = word_choose.find(ans_let)
            if ans_pos != -1 and len(ans_let) == 1:
                word_cipher = word_cipher[:ans_pos] + ans_let + word_cipher[ans_pos+1:]
                print(f"Ваше количество жизней: {lives}\n")
            elif ans_let == word_choose:
                print(f"Вы угадали слово!\n"
                      f"Загаданное слово:{word_choose.capitalize()}\n"
                      f"Ваше количество жизней: {lives}\n")
                break
            else:
                lives -= 1
                print(f"Ваш ответ неверный!\n"
                      f"Ваше количество жизней: {lives}\n")
            if word_cipher == word_choose:
                print(f"Вы угадали слово!\n"
                      f"Загаданное слово:{word_choose.capitalize()}\n"
                      f"Ваше количество жизней: {lives}\n")
                break
            if lives == 0:
                print(f"Вы проиграли!\n")

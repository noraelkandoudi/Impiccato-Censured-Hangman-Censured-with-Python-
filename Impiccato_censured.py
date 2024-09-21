import random
from words import bestemmie_list


def get_word():
    word = random.choice(bestemmie_list)
    return word.upper()


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    lettere_indovinate = []
    parole_indovinate = []
    tentativi = 6
    print("Okay giochiamo ad indovina la Bestemmia! ihihih :))   ")
    print(display_hangman(tentativi))
    print(word_completion)
    print("\n")
    while not guessed and tentativi > 0:
        guess = input("Indovina una lettera della bestemmia o proprio la bestemmia per intero! Wow : ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in lettere_indovinate:
                print("\nHai appena indovinato una lettera della bestemmia! wow :P. ", guess)
            elif guess not in word:
                print(guess, "\nNO! La lettera inserita non è presente nella bestemmia :((  \n))")
                tentativi -= 1
                lettere_indovinate.append(guess)
            else:
                print("Oh shit ! Good job bro davvero! ,", guess, "\nla cazzo di lettera è presente nella bestemmia!\n")
                lettere_indovinate.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in parole_indovinate:
                print("\nHai indovinato la bestemmia ! :PP\n ", guess)
            elif guess != word:
                print(guess, "\nPerdente\n")
                tentativi -= 1
                parole_indovinate.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print("\nNon è valido! Ritenta perdente.\n")
        print(display_hangman(tentativi))
        print(word_completion)
        print("\n")
    if guessed:
        print("\nCongratulazioni! Hai indovinato cazzo !\n")
    else:
        print("\nBello hai perso le vite! " + word + ". Maybe next time!\n")


def display_hangman(tentativi):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tentativi]


def main():
    word = get_word()
    play(word)
    while input("Vuoi perdere altro tempo ? (Yes / No ) ").upper() == "Yes":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()
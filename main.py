import random

hangman_pics = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']

words = "aigle python baleine bouc chat chien minette marantz puma putois souris taupe mule cygne poisson furet " \
        "coyote grenouille salamandre tortue".split()


# la fonction get_random_word() avec comme paramètre un argument de type liste. Elle renvoie un mot choisi dans la
# liste.
def get_random_word(word_list):
    # returns a random word among those in the list
    word_index = random.randint(0, len(word_list) - 1)
    # Nous stockons dans word_index un index choisi de façon aléatoire en appelant la fonction RANDINT() avec cette
    # fois deux arguments. Le premier est 0 (le premier index possible), le second est la valeur de l'expression len(
    # word_list)-1, pour le dernier index possible dans word_list.
    return word_list[word_index]


def display_board(missed_letters, correct_letters, secret_word):
    print(hangman_pics[len(missed_letters)])
    print()

    print("Mauvaises lettres :", end=" ")
    for letter in missed_letters:
        print(letter, end=" ")
    print()

    blanks = "_" * len(secret_word)
    # remplace les tirets par les lettres correctement devinées.
    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
        # affiche le mot secret avec des espaces entre les lettres.
    for letter in blanks:
        print(letter, end=" ")
    print()

    def get_guess(already_guessed):
        # affiche la lettre saisie par le joueur. S'assure qu'il s'agit d'une unique lettre et de rien d'autre
        while True:
            print("propose une lettre")
            guess = input()
            guess = guess.lower()
            if len(guess) != 1:
                print("propose une seule lettre")
            elif guess in already_guessed:
                print("Tu as déjà demandé cette lettre")
            elif guess not in "abcdefghijklmnopqrstwxyz":
                printt("Propose une lettre")
            else:
                return guess

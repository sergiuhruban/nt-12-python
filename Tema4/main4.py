import random

word_list = ['Cluj', 'Mures', 'Sibiu', 'Alba', 'Bistrita', 'Bacau', 'Iasi', 'Galati', 'Pitesti', 'Valcea']
chosen_word = random.choice(word_list)
display = []

for letter in chosen_word:
    display.append("_")
print(' '.join(display))

count = 0

while '_' in display and count < 3:
    print('Guess:')
    guess = input()
    k = list(chosen_word)

    if guess in k:

        while guess in k:
            display[''.join(k).find(guess)] = guess
            k[''.join(k).find(guess)] = ' '
    else:

        count += 1
        print('Guesses left = ', 3 - count)
    print(' '.join(display))
if count >= 3:
    print('You lost. The word was', chosen_word)

else:
    print('You won! The word was', chosen_word)
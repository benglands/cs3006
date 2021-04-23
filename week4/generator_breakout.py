def generate_letters():
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'

    alpha_lower_generator = (letter for letter in alpha_lower)

    while True:
        try:
            print(next(alpha_lower_generator))
        except StopIteration:
            break

def generate_three_letter_permuations():
    alpha_lower = 'abcdefghijklmnopqrstuvwxyz'
    alpha_lower_mod = len(alpha_lower)

    alpha_lower_generator1 = (letter for letter in alpha_lower)
    alpha_lower_generator2 = (letter for letter in alpha_lower)
    alpha_lower_generator3 = (letter for letter in alpha_lower)

    letter1 = next(alpha_lower_generator1)
    letter2 = next(alpha_lower_generator2)
    letter3 = next(alpha_lower_generator3)
    print(letter1+letter2+letter3)

    # Add additional logic to print out remaining permutations
    # try-except block with StopIteration catch will not need to be used
    # Hint: alpha_lower_mod will need to be used

if __name__ == '__main__':
    print('generate_letters\n')
    generate_letters()
    print('\ngenerate_three_letter_permuations\n')
    generate_three_letter_permuations()

 
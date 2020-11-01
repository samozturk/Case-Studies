import string
import sys

def solution(a, b ):
    # Remove space chars
    # Sort <a> and <b> strings
    sorted_a = sorted(a)
    sorted_b = sorted(b)

    # Get all the letter in alphabet(English)
    alphabet_lowercase = list(string.ascii_lowercase)
    alphabet_uppercase = list(string.ascii_uppercase)

    alphabet = alphabet_lowercase + alphabet_uppercase + list(' ')

    # Create a dictionary to count letter occurances for <a> and <b> strings
    dictofchars = {i: 0 for i in alphabet}
    dict_a = dictofchars.copy()
    dict_b = dictofchars.copy()

    # Record count of letters in dictionaries
    for i in a:
        dict_a[i] += 1
    for i in b:
        dict_b[i] += 1

    # Create a difference dictionary to record subtraction(<a> - <b>) of count recordings
    difference_dict = dictofchars.copy()

    # Check if <a> and <b> are anagrams
    if(sorted_a == sorted_b):
        print('They are anagram')
    else:
        # Subtract(<a> - <b>) of count recordings
        for a_key, a_value in dict_a.items():
            difference_dict[a_key] = dict_a[a_key] - dict_b[a_key]
        # Create how many words are different in both strings
        a_diff = 0
        b_diff = 0
        for key, value in difference_dict.items():
            if value > 0:
                a_diff += value
            elif value < 0:
                b_diff += abs(value)
        print('Remove ', str(a_diff), 'characters from ', str(a), 'and', str(b_diff), 'characters from ', str(b) )

if __name__ == '__main__':
    cmdargs = list(sys.argv)
    #solution(a=sys.argv[1][2:], b=sys.argv[2][2:])

    a_index = sys.argv.index('a:')
    b_index = sys.argv.index('b:')

    arg_a = ' '.join(sys.argv[a_index+1:b_index])
    arg_b = ' '.join(sys.argv[b_index+1:])
    solution(a=arg_a, b=arg_b)
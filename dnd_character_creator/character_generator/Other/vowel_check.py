def vowel_check(string):
    vowels = ['A','a','E','e', 'I', 'i', 'O', 'o', 'U', 'u']
    for char in vowels:
        if string[0] == char:
            return 'an'
    return 'a'

def is_palindrome(word):
    palindrome = True
    length = len(word)
    if length == 0 or length == 1:
        return True
    if word[0] == word[-1]:
        word = word[1:-1]
        palindrome = is_palindrome(word)
    else:
        palindrome = False
    return palindrome

while True:
    word_inputted = input('Enter a word to check for palindrome: ')
    word_inputted = str.upper(word_inputted)
    print(is_palindrome(word_inputted))

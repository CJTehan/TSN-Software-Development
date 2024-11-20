# Algorithm using iteration:

def is_palindrome(text):
    '''
    Check if a given text is a palindrome using iteration.
    '''
    processed_text = text.lower()
    processed_text = ''.join(ch for ch in processed_text if ch.isalnum()) # Remove spaces/punctuation
    left = 0
    right = len(processed_text) - 1
    while left < right:
        if processed_text[left] != processed_text[right]:
            return False
        left += 1
        right -= 1
    return True
# Get user input
user_input = input('Enter a word or phrase: ')
# Check if it's a palindrome
if is_palindrome(user_input):
    print('It\'s a palindrome!')
else:
    print('It\'s not a palindrome.')
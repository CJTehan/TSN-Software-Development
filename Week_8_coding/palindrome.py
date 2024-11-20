# Algorithm using slicing:
def is_palindrome(text):
    '''
    Check if a given text is a palindrome using string slicing.
    '''
    processed_text = text.lower()
    processed_text = ''.join(ch for ch in processed_text if ch.isalnum()) # Remove spaces/punctuation
    reversed_text = processed_text[::-1] # Reverse the processed text using slicing
    if processed_text == reversed_text:
        return True
    else:
        return False
# Get user input
user_input = input('Enter a word or phrase: ')
# Check if it's a palindrome
if is_palindrome(user_input):
    print('It\'s a palindrome.')
else:
    print('It\'s not a palindrome.')

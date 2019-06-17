#PF-Assgn-31
def check_palindrome(word):
    if word[::-1] == word:
        return 1
    else:
        return 0

status=check_palindrome("malayalam")
if(status):
    print("word is palindrome")
else:
    print("word is not palindrome")

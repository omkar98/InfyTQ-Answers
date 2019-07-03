#PF-Assgn-40
def is_palindrome(word):
    word.lower()
    if word[::-1].lower() == word.lower():
        return 1
    else:
        return 0

result=is_palindrome("Madam")
if(result):
    print("The given word is a Palindrome")
else:
    print("The given word is not a Palindrome")

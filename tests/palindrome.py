#palindrome

def isPalindrome(word):
    print("Word is {}".format(word))
    length = len(word)
    mid_point = length / 2

    print ("Length of word is {}".format(length))

    for i in range(0, mid_point+1):
        if (word[i].lower() != word[-(i+1)].lower()):
            return False
    return True


result = isPalindrome("Deleveled")
print result

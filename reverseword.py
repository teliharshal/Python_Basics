# reverse the word of a senternce without using build in function

def reverse(Sentence: str):
    word = Sentence.split()
    left , right = 0 , len(word) - 1

    while left < right:
        word[left], word[right] = word[right], word[left]
        left += 1
        right -= 1

    return " ".join(word)

print(reverse("Hello word")) 

    
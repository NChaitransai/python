def count_vowels(sentence):
    v=["a","e","i","o","u"]
    count=0
    for char in sentence.lower():
     if char in v:
        count+=1
        return count
     s=input()
    print(count_vowels(s))
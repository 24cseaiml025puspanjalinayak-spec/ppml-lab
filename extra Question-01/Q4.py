text = input("enter a string :- ")
vowel = 0
consonant = 0
for char in text:
    if char in "aeiouAEIOU":
        vowel += 1
    else:
        consonant += 1
print("Reversed string : ",text[::-1])
print("Number of vowels : ", vowel)
print("Number of consonants : ", consonant)
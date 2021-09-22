# Return the number (count) of vowels in the given string.

# We will consider a, e, i, o, u as vowels (but not y).

# The input string will only consist of lower case letters and/or spaces.

# ex:
word = ('hello_world')

def num_vowels(word):
    vowels = 0
    for i in word:
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            vowels = vowels + 1
            
    return vowels
            
print(num_vowels(word))
def oddSum(x):
    """finds the sum of odd numbers from x numbers of input from user"""
    addition = 0
    for i in range(x+1): #iterating through the numbers 
        if i % 2 !=0:
            addition += i
    return addition
x = int(input("enter n numbers here:")) #taking input from user
print(oddSum(x)) #calling the function

def palindrome(word):
    """checking if a user input word is a palindrome or not"""
    word = word.lower() #lowercasing the alphabets if any in uppercase
    pal = ''

    for letter in word: #iterating through the input word
        pal += letter 

    if pal == word:
        return True
    else:
        return False

word = input("Enter a word:") #taking input from user

if palindrome(word): #calling the function and printing the appropraite output 
    print('The word is a palindrome')
else:
    print('The word is not palindrome')

def vowelOrCons(name):
    """counting the number of vowels and consonants in a user input name"""
    name = name.lower() #lowercasing the alphabets if any in uppercase
    vowels = 'aeiou'
    v = 0
    c = 0
    for char in name: #iterating through the input name
        if char in vowels:
            v += 1
        else:
            c += 1
    return v, c
name = input('enter a name:') #taking input from user
print(vowelOrCons(name)) #calling the function and printing the output 


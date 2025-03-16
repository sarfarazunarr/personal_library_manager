# This is Assignment part 2 it is not connected with library project

# Challenge 1
# Write a function that takes a string as input and returns the reversed string.
def reverseUs(str):
    return str[::-1]

# Challenge 2
# Write a function that counts the number of vowels (a, e, i, o, u) in a string (case-insensitive).
def countVowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in string:
        if vowels.__contains__(char):
            count += count + 1
    return count;
        


# Challenge 3
# Write a function that takes a non-negative integer and returns the sum of its digits.
def countPostivies(value):
    string = str(value)
    sum = 0
    if len(string) == 1:
        sum = int(string)
    else:
        for char in string:
            sum += int(char)
    return sum;

print("Welcome to Challenger!")
sample = input("Enter string to reverse: ")
print(reverseUs(sample))

print("Count Vowels")
sample = input("Enter string to count vowels: ")
print(countVowels(sample))

print("Get Sum of All digits")
sample = int(input("Enter Value: "))
print(countPostivies(sample));

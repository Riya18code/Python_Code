
# Take a string as input from the user
text = input("Enter a string: ")

# Initialize counters to count vowels and consonants
vowels = 0
consonants = 0

# Convert the string to lowercase and check each character
for ch in text.lower():

    # Check whether the character is a vowel
    if ch in "aeiou":
        vowels = vowels + 1  # Increase vowel count by 1

    # Check whether the character is an alphabet letter
    # If it is not a vowel, it is a consonant
    elif ch.isalpha():
        consonants = consonants + 1  # Increase consonant count by 1

# Display the total number of vowels
print("Number of vowels:", vowels)

# Display the total number of consonants
print("Number of consonants:", consonants)

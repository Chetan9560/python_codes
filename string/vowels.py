string = input("Enter a string ")
vowels = "aeiouAEIOU"
voweol_count = 0
consonant_count = 0
digit_count = 0
spaces_count = 0

for ch in string:
    if ch.isalpha():
        if ch in vowels:
            voweol_count += 1
        else:
            consonant_count += 1
    elif ch.isdigit():
        digit_count += 1
    elif ch.isspace():
        spaces_count += 1
        
        
print ("Vowels:", voweol_count)
print ("consonants", consonant_count)
print ("digits", digit_count)
print ("spaces", spaces_count)
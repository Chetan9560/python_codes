string = str(input("Enter a string: "))

cleaned = string.replace(" ", " ").lower()

if cleanesd == cleaned[::-2]:
    print (" it is palindrome")
else:
    print (" it is not palindrome ")
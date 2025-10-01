string = str(input("enter a string: "))

frequency ={}

for char in string:
    if char in frequency:
        frequency[char] +=1
    else:
        frequency[char] =1
print( "carecter frequency")
for char, count in frequency.items():
    print("frequency of", char, "is", count)
        
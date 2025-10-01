string1 = str(input("enter frist string:"))
string2 = str(input("enter second stirng: "))
 
def is_anagram(string1, string2):
    string1 = string1.replace(" "," ").lower()
    strimg2 = string2.replace(" ", " ").lower()

    return sorted(string1) == sorted(string2)

if is_anagram(string1, string2):
    print("the two str is anagram")
else:
    print("the two str is not anagram")
    


    
    
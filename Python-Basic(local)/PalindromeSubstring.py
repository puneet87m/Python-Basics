
def isPalindrome(s):
    # Calling reverse function
    rev = s[::-1]
 
    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False

def countSubstrings(s):
    length = len(s)
    count = 0
    
    if not length:
        return count
    
    for i in range(length):
        counter=i+1
        while counter <= length:
            if isPalindrome(s[i:counter]):
                count += 1
            counter += 1      
    return count

str=input("Enter your String")
x=countSubstrings(str)
print("String", str," has total", x , "plaindrome in it.")

# Write a function that gets as parameters two strings. The function returns the number of characters that the strings have in common. Each character counts only once, e.g., the strings "bee" and "peer" only have one character in common (the letter “e”). You can consider capitals different from lower case letters. Note: the function should return the number of characters that the strings have in common, and not print it. To test the function, you can print the result in your main program.

def SumOfTwoStrings (str1, str2):
        common=0
        for letter in str1:
                if letter in str2:
                        common+=1
        return common

def dublRemover( s1 ):
        for letter in s1:
                s2=s1
                while s2.find( letter ) != -1:
                        s1=s2
                        s2=s2.replace( letter, '', 1 )
        return s1

print ("Let's check how many characters are the same in two different strings" )
str1 = dublRemover( input("Enter your first string: " ) )
str2 = dublRemover( input("Enter your second string: " ) )

print ("The number of common characters is",SumOfTwoStrings (str1, str2))


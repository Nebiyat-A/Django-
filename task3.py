/*question 1 */
numbers=["%02d" % x for x in range (0,100)]
print (numbers)

/*question 2*/

myInput = str(input("please enter the pattern to be printed: "))
vowel = 'AEIOUaeiou'
if myInput not in vowel:
    for a in range(0,7):
        for b in range(a):
            print(myInput,end='')
        print(myInput)
elif len(myInput) > 1:
    print("character canot be more than 1 letter")
else:
    print("you can't enter vowels")

    /*question three*/
input("please enter the word")
def isPalindrome(s):
    return s == s[::-1]
 
if isPalindrome:
    print("Yes, it is palindrome.")
else:
    print("No, it is not palindrome.")

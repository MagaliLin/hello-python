# In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
def count_substring(string, sub_string):
    iCount = 0
    sResult = string
    iPos = sResult.find(sub_string)
    while iPos > -1:
       iCount += 1
       sResult = sResult[iPos+1:]
       iPos = sResult.find(sub_string)
    return iCount

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

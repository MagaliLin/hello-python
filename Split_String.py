# Consider the following:
# A string, , of length where
# An integer,
# , where is a factor of
# We can split
# into subsegments where each subsegment, , consists of a contiguous block of characters in . Then, use each to create string
# such that:
    # The characters in 
# are a subsequence of the characters in
# Any repeat occurrence of a character is removed from the string such that each character in
# occurs exactly once. In other words, if the character at some index in occurs at a previous index in , then do not include the character in string
# Given
# Input Format
# The first line contains a single string denoting
# The second line contains an integer, , denoting the length of each subsegment.
def merge_the_tools(string, k):
    n = len(string)
    k = int(k)
    lSub = [string[i:i+k] for i in range(0, n, k)]
    for xSub in lSub:
        xFinal = xSub[0:1]
        for i in range(1, k):
            if xFinal.rfind(xSub[i:i+1]) == -1:
                xFinal += xSub[i:i+1] 
        print(xFinal)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

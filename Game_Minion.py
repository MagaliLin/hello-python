# Kevin and Stuart want to play the 'The Minion Game'.
# Game Rules
# Both players are given the same string,
# Both players have to make substrings using the letters of the string
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.
# Scoring
# A player gets +1 point for each occurrence of the substring in the string
//github
def minion_game(string):
    tVowel = ('A', 'E', 'I', 'O', 'U') 
    kevin_Sco = 0
    stuart_Sco = 0
    n = len(string)
    for i in range(n):
        if string[i:i+1] in tVowel:
            kevin_Sco += n - i
        else:
            stuart_Sco += n - i
               # print('zu' + word)
    if  kevin_Sco == stuart_Sco:
        print('Draw')
    elif kevin_Sco > stuart_Sco:
        print('Kevin ' + str(kevin_Sco))
    else:
        print('Stuart ' + str(stuart_Sco))

if __name__ == '__main__':
    s = input()
    minion_game(s)

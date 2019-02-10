# A valid UID must follow the rules below:

    # It must contain at least 

# uppercase English alphabet characters.
# It must contain at least
# digits ( -
# ).
# It should only contain alphanumeric characters (
# - , - & -
# ).
# No character should repeat.
# There must be exactly
# characters in a valid UID.

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
regexp = r'^(?=(?:[4-6]))(?=(?:[0-9]))'
def UID_Verif(string):
    regexp = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:.*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
    if re.match(regexp, string) is None:
        return 'Invalid'
    return 'Valid'

if __name__ == '__main__':
    sIUD = ''
    n = int(input())
    for _ in range(n):
        sUID = input()
        print(UID_Verif(sUID))

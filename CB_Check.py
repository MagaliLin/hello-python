# A valid credit card from ABCD Bank has the following characteristics:

# ► It must start with a , or .
# ► It must contain exactly digits.
# ► It must only consist of digits (-).
# ► It may have digits in groups of , separated by one hyphen "-".
# ► It must NOT use any other separator like ' ' , '_', etc.
# ► It must NOT have or more consecutive repeated digits. 
#useful ressources
#   https://buzut.fr/la-puissance-des-regex/
#   https://regex101.com/
#   https://regexone.com/lesson
import re

def re_Verif(string):
    #regexp = r'^(?=(?:[a-z\d]*[A-Z]){2})(?=(?:.*\d){3})(?:([a-zA-Z\d])(?!.*\1)){10}$'
    regexp = r'(?=((4|5|6)\d{3})((-?(\d{4})){3}))'
    if re.match(regexp, string) is None:
        return 'Invalid'
    str_digits = string.replace('-','')
    if len(str_digits) > 16 :
        return 'Invalid'
    regexp = r'(\d)+\1{3}'
    if re.match(regexp, str_digits) != None:
        return 'Invalid'
    return 'Valid'

if __name__ == '__main__':
    sIUD = ''
    n = int(input())
    for _ in range(n):
        sIn = input()
        print(re_Verif(sIn))

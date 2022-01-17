def ispalindrome(mot):
    mot = mot.replace(' ', '')
    if len(mot) <= 1:
        return True
    elif mot[0] == mot[-1]:
        return ispalindrome(mot[1:-1])
    else:
        return False
print(ispalindrome('emile nu a une lime'))

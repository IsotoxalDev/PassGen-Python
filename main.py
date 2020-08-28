from getpass import getpass
import string
import random as r
#masterPass = getpass()
passwdlen = 16
def pwdgen(length = 16):
    finalPwdlist = []
    finalPwd = ''
    caplett = string.ascii_uppercase
    smallett = string.ascii_lowercase
    for _i in range(length):
        n = r.randrange(62)
        if n < 10:
            finalPwdlist.append(str(n))
        elif n < 36:
            finalPwdlist.append(caplett[(n-10)])
        else:
            finalPwdlist.append(smallett[(n-36)])
    for k in finalPwdlist:
        finalPwd += k
    return finalPwd
pwd = pwdgen(5)
while pwd != ('felix'):
    print(pwd)
    pwd = pwdgen(5)
print(pwd)
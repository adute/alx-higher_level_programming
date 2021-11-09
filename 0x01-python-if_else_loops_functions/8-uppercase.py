#!/usr/bin/python3
def uppercase(str):
    strNew = ''
    for i in range(len(str)):
        if(str[i] >= 'a' and str[i] <= 'z'):
            strNew = strNew + chr((ord(str[i]) - 32))
        else:
            strNew = strNew + str[i]

    print(strNew.format())


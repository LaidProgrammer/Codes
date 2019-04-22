CDICT = 'абвгдеёжзийклмнопрстуфхцчщьъыьэюя'
HCDICT = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
LDICT = 'abcdefghijklmnopqrstuvwxyz'
HLDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DICTS = [CDICT, HCDICT, LDICT, HLDICT]

def caesar(str0='', dicts=DICTS, step=1):
    str1=''
    for i in str0:
        k = False
        for j in dicts:
            if i in j:
                str1+=(j[(j.index(i) + step) % len(j)])
                k = True
                break
        if not k:
            str1 += i
    return str1

CDICT = 'абвгдеёжзийклмнопрстуфхцчщьъыьэюя'
HCDICT = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
LDICT = 'abcdefghijklmnopqrstuvwxyz'
HLDICT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
DICTS = [CDICT, HCDICT, LDICT, HLDICT]


#Function caesar(str0 : str = '' - input string,
# dicts: list of strings = DICTS - list of all dictionaries,
# step : int - encoding step)
#Returns caesar code of given string with given step
def caesar(str0:str='', dicts:list=DICTS, step:int=1): 
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

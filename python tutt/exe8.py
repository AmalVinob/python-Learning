# oh solder prettify my foleder
"""
path as input
dictinory,file formate

"""
import os

def fileopener(file):
    opener = open(file)
    l = opener.read()
    var = l.split("\n")
    # print(l)
    opener.close()
    return var

def army(pathn,file,png):
    pathn = pathn
    file = file
    os.chdir(pathn)
    count = 0
    var = fileopener(file)
    for f in os.listdir(pathn):
        f_name, f_png = os.path.splitext(f)
        print(f_name)
        if f_png == f'.{png}':
            new_name = f'{str(count)}{f_png}'
            count +=1
            os.rename(f,new_name)
        if f_name not in var:
            tn = f_name.title()
            new_name = f'{tn}{f_png}'
            os.rename(f,new_name)
        else:
            pass

if __name__ == '__main__':
    pathn = r'C:\Users\amalv\OneDrive\Desktop\tutee'
    file = r"C:\Users\amalv\PycharmProjects\python tutt\soilder"
    png = "jpg"
    army(pathn,file,png)
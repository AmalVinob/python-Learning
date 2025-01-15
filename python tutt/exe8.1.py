import os

def soilders(path,file,format):
    os.chdir(path)
    i = 1
    files = os.listdir(path)
    print(files)
    with open(file) as f:
        filelist = f.read().split("\n")
        print(filelist)

    for file in files:
        if file not in filelist:
            os.rename(file,file.capitalize())
        if os.path.splitext(file)[1] == format:
            os.rename(file, f"{i}{format}")
            i+=1

soilders(r"C:\Users\amalv\OneDrive\Desktop\tutee",r"C:\Users\amalv\PycharmProjects\python tutt\soilder",".jpg")
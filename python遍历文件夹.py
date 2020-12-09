import os

def WalkThruDir(dir):
    g = os.walk(dir)
    for path,dirlist,filelist in g:
        for file in filelist:
            print(os.path.join(path,file))
WalkThruDir("e:/pythonstudy")            
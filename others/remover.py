from pathlib import Path
import os

file = Path('../untracked.txt')

def getDuplicates():
    with open(file, 'r') as f:
        while True:
            line = f.readline()
            if not line:
                break
            filename = line.strip()
            if len(filename) == 0:
                continue
            filename = filename.replace("/usr/src/app/upload/", "/home/chauv/imports-backup/")
            filename_new = "/home/chauv/imports-backup/moved/" + filename.split('/')[-1]
            if os.path.exists(filename):
                os.rename(filename, filename_new)
                print ("done :" + filename)

if __name__ == '__main__':
    getDuplicates()
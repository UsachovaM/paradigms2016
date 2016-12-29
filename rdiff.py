import os
import sys
import difflib
from difflib import *

if __name__ == "__main__":
    folder1 = sys.argv[1]
    files1 = os.listdir(folder1)
    folder2 = sys.argv[2]
    files2 = os.listdir(folder2)
    files = sorted(set(files1 + files2))
    for file in files:
        if file not in files2:
            print('Only in ', folder1, ': ', file, sep='')
        elif file not in files1:
            print('Only in ', folder2, ': ', file, sep='')
        else:
            name1 = os.path.join(folder1, file)
            with open(name1) as file1:
                sfile1 = file1.readlines()
            name2 = os.path.join(folder2, file)
            with open(name2) as file2:
                sfile2 = file2.readlines()
            sys.stdout.writelines(unified_diff(sfile1,
                                               sfile2,
                                               fromfile=name1,
                                               tofile=name2))

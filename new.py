#!~/Pattern_Matching python
from os import system
import os
import fnmatch

def move_dir(a):

    path = os.getcwd()
    path += "/"
    path += a

    os.chdir(path)
    print os.getcwd()


def leave_dir():
    count = 0
    newpath = []
    path = os.getcwd()
    for i in range(len(path)):
        if(path[i] == '/'):
            count += 1

    if(count == 1):
        print  "In the outermost directory...can't leave"
        return 0
    else:
        n = len(path)

        i = n - 1
    
        while(path[i] != '/'):
            i -= 1

        j = 0
        while(j < i):
            newpath.append(path[j])
            j += 1
    
        path = ""
        for i in newpath:
            path = path + i
    
        os.chdir(path)



def print_dir():

    path = os.getcwd()
    all_files = os.listdir(path)
    contents=[]
    directories = []
    
    
    for i in all_files:
        if i[0] == '.':
            continue
        else:
            contents.append(i)

    for file in contents:
         if(fnmatch.fnmatch(file, "*.txt") or fnmatch.fnmatch(file, "*.md") or fnmatch.fnmatch(file, "*.c") or fnmatch.fnmatch(file, "*.py")):
            continue
         else:
            directories.append(file)
    
    if(len(directories) == 0):
        print "No directories..."
        return 0
    directories.sort()
    print "\nDirectories:"
    for i in directories:
        print i + "   ",

    ch = raw_input("\n\nEnter directory: ")

    if(ch in directories):
        return ch
    else:
        print "Invalid directory"
        return 0

def print_file():
    
    path = os.getcwd()
    #print path
    all_files = os.listdir(path)
    contents=[]

    for i in all_files:

        if i[0] == '.':
            continue
        else:
            contents.append(i)


    files = []
    for file in contents:
        if(fnmatch.fnmatch(file, "*.txt") or fnmatch.fnmatch(file, "*.md") or fnmatch.fnmatch(file, "*.c") or fnmatch.fnmatch(file, "*.py")):
            files.append(file)

    if(len(files) == 0):
        print "No files..."
        return 0

    files.sort()
    print "\nFiles:"
    for i in files:
        print i + "   ",

    print "\n"

    



x = 0

while(x != 4):
    path = os.getcwd()

    print "\n\nInside Directory: " + path
    print "1.Choose directory\n2.Work on a file\n3.Leave directory\n4.Exit"

    x = input()

    if(x == 1):
        a = print_dir()
    
        if a != 0:
            move_dir(a)
    if(x == 2):
        print_file()
        system("work")
 
    if(x == 3):
        leave_dir()


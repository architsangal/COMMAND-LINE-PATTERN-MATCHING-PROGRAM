#!~/Pattern_Matching python3
import re
from os import system

def inputting():

    choice = str(input("\n\t\t\t1) Searching\n\t\t\t2) Replacing\n\t\t\tTo quit Enter q...\n\n\t\t\tEnter Your Choice : "))
    if(choice == "1"):
        return 1
    elif(choice == "2"):
        return 2
    elif(choice == "q" or choice == "Q"):
        return 3
    else:
        system("clear")
        print("\n\t\t\tInvalid Input\n\t\t\tTry Again\n")
        return inputting()

def searching():

    system("clear")
    choice = str(input("\n\t\t\t1)Searching For Exact String\n\t\t\t2)Searching For A USER FRIENDLY Format\n\t\t\t3)Search By Pattern Which You Have(Recommended For Professionals ONLY)\n\t\t\t4)Searching For A Word With Starting Known\n\t\t\t5)Searching For A Word With Ending Known\n\t\t\tEnter your choice : "))
    system("clear")
    if(choice == "1"):
        exact()
    elif(choice == "2"):
        format()
    elif(choice == "3"):
        format(1)
    elif(choice == "4"):
        start()
    elif(choice == "5"):
        end()
    else:
        system("clear")
        print("\n\t\t\tInvalid Input\n\t\t\tTry Again\n")
        searching()

def exact():
    
    string = str(input("\n\n\t\t\tNOTE : DONOT USE \"\\\" IN YOUR SEARCH\n\n\t\t\tEnter The String To Be Searched : "))
    l = re.findall(string,data)
    number = len(l)
    start_l=[]
    start_l.append(string)
    temp_data = data
    if(number == 0):

        system("clear")
        print("\"" + string + "\"" + " is not found in " + "\"" + files + "\"")
        exact()

    else:
        
        c=0
        for i in range(number):
            
            element = re.search(string,temp_data)
            start_l.append(element.start()+c)
            temp_data = temp_data[element.end():len(temp_data)] 
            c += element.end()
        system("clear")
        store_txt(start_l)
        print(start_l)

def format(k=0):

    pattern = ""
    l=[]
    if(k==0):
        print("\n\t\t\tEnter the format BELOW\n\n\t\t\te.g.\n\t\t\tif input is 14/03/2000 it will find all dates of format dd/mm/yyyy")
        print("\t\t\tBut if input is dd/mm/yyyy it will find all the substring e.g. aa/bb/cccc")
        print("\t\t\tProgram can differentiate between alphabets(It is case sensitive.) and digits.\n\n\t\t\tNOTE : DONOT USE \"\\\" IN YOUR SEARCH")
        char = str(input("\n\n\t\t\tEnter The Format : "))
        for i in char:
            if(i<="9" and i>="0"):
                pattern += r"\d"
            elif(i<="z" and i>="a"):
                pattern += r"[a-z]"
            elif(i<="Z" and i>="A"):
                pattern += r"[A-Z]"
            else:
                pattern += i
        l = re.findall(pattern,data)
    else:
        l = re.findall(input("\n\n\t\t\tEnter The Format : "),data)
    
    number = len(l)

    #removing duplicate elements of list
    temp_list=[]
    for j in l:
        if j not in temp_list:
            temp_list.append(j)

    l = temp_list
 
    inFile=[]
    if(number == 0):

        system("clear")
        print("Not found in " + "\"" + files + "\"\n\n\n")
        format(k)

    else:
        
        for j in l:
            
            string = j
            c=0
            start_l=[]
            start_l.append(j)
            temp_data = data
            num = re.findall(j,data)
            for i in range(len(num)):
                
                element = re.search(string,temp_data)
                start_l.append(element.start()+c)
                temp_data = temp_data[element.end():len(temp_data)] 
                c += element.end()
        
            inFile.append(start_l)
        system("clear")
        store_txt(inFile)
        print(inFile)

def start():

    l = re.findall(input("\n\n\t\t\tEnter The Starting Of letters With \'\\b\' At The Starting\n\t\t\te.g. if starting is \"ARC\" enter it as \"\\bARC\n\t\t\tEnter : "),data)
    number = len(l)

    #removing duplicate elements of list
    temp_list=[]
    for j in l:
        if j not in temp_list:
            temp_list.append(j)

    l = temp_list

    inFile=[]

    if(number == 0):

        system("clear")
        print("Not found in " + "\"" + files + "\"\n\n\n")
        start()

    else:
        
        for j in l:
            
            string = j
            c=0
            start_l=[]
            temp_data = data
            num = re.findall(j,data)
            for i in range(len(num)):
                
                element = re.search(string,temp_data)
                if(element.start() == 0 or temp_data[element.start()-1] == " " or temp_data[element.start()-1] == "\n"):
                    start_l.append(element.start()+c)
                temp_data = temp_data[element.end():len(temp_data)] 
                c += element.end()
        
            inFile.append(start_l)
        
        ans = []
        for i in inFile[0]:
            j=i
            stringing = ""
            while(data[j] != " " and data[j] != "\n"):
                stringing = stringing + data[j]
                j += 1
            ans.append([stringing,i])
            print([stringing,i])
        
        store_txt(ans)

def end():

    l = re.findall(input("\n\n\t\t\tEnter The Ending Of Word With \'\\b\' At The End\n\t\t\te.g. if ending is \"GAL\" enter it as \"ARC\\b\"\n\t\t\tEnter : "),data)
    number = len(l)

    #removing duplicate elements of list
    temp_list=[]
    for j in l:
        if j not in temp_list:
            temp_list.append(j)

    l = temp_list
 
    inFile=[]
    if(number == 0):

        system("clear")
        print("Not found in " + "\"" + files + "\"\n\n\n")
        end()

    else:
        
        for j in l:
            
            string = j
            c=0
            start_l=[]
            temp_data = data
            num = re.findall(j,data)
            for i in range(len(num)):
                
                element = re.search(string,temp_data)
                if(temp_data[element.end()] == len(temp_data) or temp_data[element.end()] == " " or temp_data[element.end()] == "\n"):
                    start_l.append(element.start()+c)
                temp_data = temp_data[element.end():len(temp_data)] 
                c += element.end()
        
            inFile.append(start_l)
        ans = []
        for i in inFile[0]:
            j=0
            c=0
            while(j != i):
                if(data[j] == " " or data[j] == "\n"):
                    c=j
                j += 1
            k=i
            while(data[k] != " " and data[k] != "\n" and k<len(data)):
                k +=1
            stringing = data[c+1:k]
            ans.append([stringing,i])
            print([stringing,i])
        
        store_txt(ans)

                
def store_txt(start_l):

    char = str(input("Do you want to store the  data in a file ? (y or n) : "))
        
    if(char == "y" or char == "Y"):

        name = str(input("Enter the name of file : "))
        system("mkdir -p txt\ files")
        name = open(r"txt files/" + name,"w")
        name.write(str(start_l))
        name.close()

#system("clear")
files = str(input("\n\n\n\t\t\tEnter The Name Of File : "))

try:

    fromFile = open(files,"r")

except FileNotFoundError :

    print("No Such File EXIST ...")

else:

    data = fromFile.read()
    while(True):
        choice = inputting()
        
        if(choice == 1):
            
            searching()
        
        elif(choice == 2):
            
            system("clear")
            original = str(input("\n\t\t\tEnter The pattern to be replaced : "))
            replace = str(input("\n\t\t\tEnter The data with which it is to be replaced : "))
            new_data = re.sub(original,replace,data)
            store_txt(new_data)
            system("clear")
            print("\n\n\n" + new_data)

        elif(choice == 3):
            break

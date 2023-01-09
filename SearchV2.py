import os
import time

def searchBothEngine(targetDirectory, target):
    print("Searching files & Folders ...")
    totalResult=0
    for root, dir, files in os.walk(targetDirectory):
        matchingVals = [x for x in files if 1+x.lower().find(target)]
        if len(matchingVals)!=0:
            totalResult=totalResult+len(matchingVals)
            print("matching files : ", matchingVals," in : ",root," Total Result : ",totalResult)
        matchingVals = [x for x in dir if 1+x.lower().find(target)]
        if len(matchingVals)!=0:
            totalResult=totalResult+len(matchingVals)
            print("matching folders : ", matchingVals," in : ",root," Total Result : ",totalResult)
    if(totalResult == 0):
        print("File or Folders Not Found")
    print("Thank you ...")

def searchFileEngine(targetDirectory, targetFile):
    print("Searching files ...")
    totalResult=0
    for root, dir, files in os.walk(targetDirectory):
        matchingVals = [x for x in files if 1+x.lower().find(targetFile)]
        if len(matchingVals)!=0:
            totalResult=totalResult+len(matchingVals)
            print("matching files : ", matchingVals," in : ",root," Total Result : ",totalResult)
    if(totalResult == 0):
        print("File Not Found")
    print("Thank you ...")

def searchFolderEngine(targetDirectory, targetFolder):
    print("Searching folder ...")
    totalResult=0
    for root, dir, files in os.walk(targetDirectory):
        matchingVals = [x for x in dir if 1+x.lower().find(targetFolder)]
        if len(matchingVals)!=0:
            totalResult=totalResult+len(matchingVals)
            print("matching folders : ", matchingVals," in : ",root," Total Result : ",totalResult)
    if(totalResult == 0):
        print("Folder Not Found")
    print("Thank you ...")

option="-1"
while(option=="-1"):
    option = input("Enter 1 for File Search \nEnter 2 for Folder Search \nEnter 3 for both: ")
    # print("option : ",option," condition 1 : ",option != "1" ," condition 1 : ", option != "2")
    if(option != "1" and option != "2" and option != "3"):
        print("Incorrect input, please try again!")
        option="-1"

targetDirectory = ""
targetFile = ""
targetFolder = ""

if option=="1":
    while(targetDirectory=="" or targetFile==""):
        if(targetDirectory==""):
            targetDirectory = input("Enter target directory : ")
        if(targetFile==""):
            targetFile = input("Enter File you want to search : ")
        if(targetDirectory=="" or targetFile==""):
            print("Enter correct data!")
    start_time = time.perf_counter()
    searchFileEngine(targetDirectory,targetFile.lower())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("Execution time in seconds : ",execution_time,"S")
elif option=="2":
    while(targetDirectory=="" or targetFolder==""):
        if(targetDirectory==""):
            targetDirectory = input("Enter target directory : ")
        if(targetFolder==""):
            targetFolder = input("Enter Folder you want to search : ")
        if(targetDirectory=="" or targetFolder==""):
            print("Enter correct data!")
    start_time = time.perf_counter()
    searchFolderEngine(targetDirectory,targetFolder.lower())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("Execution time in seconds : ",execution_time,"S")
elif option=="3":
    while(targetDirectory=="" or targetFolder==""):
        if(targetDirectory==""):
            targetDirectory = input("Enter target directory : ")
        if(targetFolder==""):
            targetFolder = input("Enter Files or Folder you want to search : ")
        if(targetDirectory=="" or targetFolder==""):
            print("Enter correct data!")
    start_time = time.perf_counter()
    searchBothEngine(targetDirectory,targetFolder.lower())
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print("Execution time in seconds : ",execution_time,"S")


# DFS algo
# Preorder Traversal

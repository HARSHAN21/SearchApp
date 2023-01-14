from tkinter import *
import tkinter.filedialog as tkFileDialog
from  tkinter import ttk
import os
import time
import threading

class searchBothEngineThread(threading.Thread):
    def __init__(self,targetDirectory,target):
        threading.Thread.__init__(self)
        self.targetDirectory = targetDirectory
        self.target=target
    def run(self):
        print("Searching files & Folders ...")
        totalResult=0
        srNo=0
        start_time = time.perf_counter()
        for root, dir, files in os.walk(self.targetDirectory):
            matchingVals = [x for x in files if 1+x.lower().find(self.target)]
            if len(matchingVals)!=0:
                totalResult=totalResult+len(matchingVals)
                print("matching files : ", matchingVals," in : ",root," Total Result : ",totalResult)
                for val in matchingVals:
                    resultTable.insert(parent='',index='end',iid=srNo,text='',values=(srNo+1,val,root))
                    srNo+=1
            matchingVals = [x for x in dir if 1+x.lower().find(self.target)]
            if len(matchingVals)!=0:
                totalResult=totalResult+len(matchingVals)
                print("matching folders : ", matchingVals," in : ",root," Total Result : ",totalResult)
                for val in matchingVals:
                    resultTable.insert(parent='',index='end',iid=srNo,text='',values=(srNo+1,val,root))
                    srNo+=1
        if(totalResult == 0):
            print("File or Folders Not Found")
        print("Thank you ...")
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        loadMsglabel.configure(text='Search Completed in '+str(execution_time)+" seconds Found "+str(totalResult)+" Results.")

class searchFileEngineThread(threading.Thread):
    def __init__(self,targetDirectory,target):
        threading.Thread.__init__(self)
        self.targetDirectory = targetDirectory
        self.targetFile=target
    
    def run(self):
        print("Searching files ...")
        totalResult=0
        srNo=0
        start_time = time.perf_counter()
        for root, dir, files in os.walk(self.targetDirectory):
            matchingVals = [x for x in files if 1+x.lower().find(self.targetFile)]
            if len(matchingVals)!=0:
                totalResult=totalResult+len(matchingVals)
                print("matching files : ", matchingVals," in : ",root," Total Result : ",totalResult)
                for val in matchingVals:
                    resultTable.insert(parent='',index='end',iid=srNo,text='',values=(srNo+1,val,root))
                    srNo+=1
        if(totalResult == 0):
            print("File Not Found")
        print("Thank you ...")
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        loadMsglabel.configure(text='Search Completed in '+str(execution_time)+" seconds Found "+str(totalResult)+" Results.")

class searchFolderEngineThread(threading.Thread):
    def __init__(self,targetDirectory,target):
        threading.Thread.__init__(self)
        self.targetDirectory = targetDirectory
        self.targetFolder=target
    
    def run(self):
        print("Searching folder ...")
        totalResult=0
        srNo=0
        start_time = time.perf_counter()
        for root, dir, files in os.walk(self.targetDirectory):
            matchingVals = [x for x in dir if 1+x.lower().find(self.targetFolder)]
            if len(matchingVals)!=0:
                totalResult=totalResult+len(matchingVals)
                print("matching folders : ", matchingVals," in : ",root," Total Result : ",totalResult)
                for val in matchingVals:
                    resultTable.insert(parent='',index='end',iid=srNo,text='',values=(srNo+1,val,root))
                    srNo+=1
        if(totalResult == 0):
            print("Folder Not Found")
        print("Thank you ...")
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        loadMsglabel.configure(text='Search Completed in '+str(execution_time)+" seconds Found "+str(totalResult)+" Results.")

selectedDirectory=""

def getDirectory():
    tempdir = tkFileDialog.askdirectory(parent=root, initialdir='C:/', title='Please select a folder')
    print(tempdir)
    # tempdir = tempdir.replace('/','\\')
    return(tempdir)

def selectDirectory():
    # print("hi")
    global selectedDirectory
    selectedDirectory=getDirectory()
    directoryLable.configure(text=selectedDirectory)
    # print("selected Directory : ",selectedDirectory)

def validateRadioOpt():
    if(radioOption.get() != 0):
        return True
    return False

def validateSelectedDirectory():
    if(selectedDirectory != ""):
        return True
    return False

def validateFileName():
    name = searchName.get()
    if(name.isalpha() or name.count('.')==1 ):
        return True
    return False

def initiateTable():
    loadMsglabel.configure(text='Searching '+searchName.get()+" in "+selectedDirectory+" ...")    
    scroll.config(command=resultTable.yview)
    scroll.pack(side=RIGHT, fill=Y)
    resultTable.pack()

def openFile():
    
    curItem = resultTable.focus()
    if(len(resultTable.item(curItem)["values"]) == 3):
        openValidateLable.configure(text='')
        print(resultTable.item(curItem)["values"])
        print("type : ",type(resultTable.item(curItem)["values"]))
        print("len : ",len(resultTable.item(curItem)["values"]))
        try:
            print("opening ",resultTable.item(curItem)["values"][2]+"/"+resultTable.item(curItem)["values"][1])
            os.startfile(resultTable.item(curItem)["values"][2]+"/"+resultTable.item(curItem)["values"][1])
        except:
            print('No application is associated with the specified file for this operation:')
    else:
        openValidateLable.configure(text='Please select proper file or folder',fg='red')

def searchFile():
    resultTable.delete(*resultTable.get_children())
    if(validateRadioOpt() == False):
        radioValidateLable.configure(text='*',fg='red')
    else:
        radioValidateLable.configure(text='')

    if(validateSelectedDirectory() == False):
        directoryValidateLable.configure(text='*',fg='red')
    else:
        directoryValidateLable.configure(text='')

    if(validateFileName() == False):
        fileSearchValidateLable.configure(text='*',fg='red')
    else:
        fileSearchValidateLable.configure(text='')

    if( validateRadioOpt() and validateSelectedDirectory() and validateFileName() ):
        print("option value : ",radioOption.get())
        print("directory value : ",selectedDirectory)
        print("file value : ",searchName.get())
        loadMsglabel.configure(text='Searching '+searchName.get()+" in "+selectedDirectory+" ...")    
        scroll.config(command=resultTable.yview)
        scroll.pack(side=RIGHT, fill=Y)
        resultTable.pack()
        totalResult=0
        if( radioOption.get() == 1 ):
            searchFileEngineThread(selectedDirectory,searchName.get().lower()).start()
        elif( radioOption.get() == 2 ):
            searchFolderEngineThread(selectedDirectory,searchName.get().lower()).start()
        else:
            searchBothEngineThread(selectedDirectory,searchName.get().lower()).start()

root = Tk()
root.title('File Search')

radioFrame = Frame(root)
fileSearchFrame=Frame(root)
directorFrame=Frame(root)
loadResultFrame=Frame(root)
resultTableFrame=Frame(root)
openFrame=Frame(root)

mainFrameRowNo=0

# Radio frame 
radioOption = IntVar()
radioFrameColNo=0
radioValidateLable = Label(radioFrame, text='')
radioValidateLable.grid(row=mainFrameRowNo,column=radioFrameColNo)
radioFrameColNo+=1
Label(radioFrame, text='What you want to search : ').grid(row=mainFrameRowNo,column=radioFrameColNo)
radioFrameColNo+=1
Radiobutton(radioFrame, text='File', variable=radioOption, value=1).grid(row=mainFrameRowNo,column=radioFrameColNo,padx=10, pady=10)
radioFrameColNo+=1
Radiobutton(radioFrame, text='Folder', variable=radioOption, value=2).grid(row=mainFrameRowNo,column=radioFrameColNo,padx=10, pady=10)
radioFrameColNo+=1
Radiobutton(radioFrame, text='Both', variable=radioOption, value=3).grid(row=mainFrameRowNo,column=radioFrameColNo,padx=10, pady=10)
radioFrameColNo+=1
mainFrameRowNo+=1

# Directory frame 
directorFrameColNo=0
directoryValidateLable = Label(directorFrame, text='')
directoryValidateLable.grid(row=mainFrameRowNo,column=directorFrameColNo)
directorFrameColNo+=1
Label(directorFrame, text='Enter directory in which you want to search : ').grid(row=mainFrameRowNo,column=directorFrameColNo)
directorFrameColNo+=1
directoryButton = Button(directorFrame, text='Select directory', command=selectDirectory).grid(row=mainFrameRowNo,column=directorFrameColNo,padx=10, pady=10)
directorFrameColNo+=1
directoryLable = Label(directorFrame, text="")
directoryLable.grid(row=mainFrameRowNo,column=directorFrameColNo,padx=10, pady=10)
directorFrameColNo+=1
mainFrameRowNo+=1

# File Search frame 
fileSearchFrameColNo=0
fileSearchValidateLable = Label(fileSearchFrame, text='')
fileSearchValidateLable.grid(row=mainFrameRowNo,column=fileSearchFrameColNo)
fileSearchFrameColNo+=1
Label(fileSearchFrame, text='Enter name to search : ').grid(row=mainFrameRowNo,column=fileSearchFrameColNo)
fileSearchFrameColNo+=1
searchName = Entry(fileSearchFrame)
searchName.grid(row=mainFrameRowNo,column=fileSearchFrameColNo,padx=10, pady=10)
fileSearchFrameColNo+=1
searchButton = Button(fileSearchFrame, text='Search', command=searchFile).grid(row=mainFrameRowNo,column=fileSearchFrameColNo,padx=10, pady=10)
fileSearchFrameColNo+=1
mainFrameRowNo+=1

# load Result Frame
loadResultFrameColno=0
loadMsglabel = Label(loadResultFrame, text='')
loadMsglabel.grid(row=mainFrameRowNo,column=loadResultFrameColno)
loadResultFrameColno+=1
mainFrameRowNo+=1

# Result Table frame 
scroll = Scrollbar(resultTableFrame)

resultTable = ttk.Treeview(resultTableFrame,yscrollcommand=scroll.set, height=20)
resultTable['columns'] = ('No', 'Name', 'Directory')

resultTable.column("#0", width=0,  stretch=NO)
resultTable.column("No",anchor=CENTER, width=40)
resultTable.column("Name",anchor=CENTER,width=400)
resultTable.column("Directory",anchor=CENTER,width=800)

resultTable.heading("#0",text="",anchor=CENTER)
resultTable.heading("No",text="No",anchor=CENTER)
resultTable.heading("Name",text="Name",anchor=CENTER)
resultTable.heading("Directory",text="Directory",anchor=CENTER)

# open Frame
openFrameColno=0
searchButton = Button(openFrame, text='Open', command=openFile).grid(row=mainFrameRowNo,column=openFrameColno,padx=10, pady=10)
openFrameColno+=1
openValidateLable = Label(openFrame, text='')
openValidateLable.grid(row=mainFrameRowNo,column=openFrameColno)
openFrameColno+=1
mainFrameRowNo+=1

# Configure all Frames
radioFrame.pack(anchor='center')
directorFrame.pack(anchor='center')
fileSearchFrame.pack(anchor='center')
loadResultFrame.pack(anchor='center')
resultTableFrame.pack(anchor='center')
openFrame.pack(anchor='center')

root.mainloop()

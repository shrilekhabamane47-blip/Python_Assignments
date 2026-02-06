import os
import time

timestamp=time.ctime()
Logfilename="Directory_File_Search%s.log" %(timestamp)
Logfilename = Logfilename.replace(" ","_")
Logfilename=Logfilename.replace(":","_")
fobj=open(Logfilename,"w")
Border = "-"*80

    
def DirectoryFileSearch(Directory,extension):
    
    fobj.write("This log file is created at "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("This is log file created by Marvellous Automation\n")
    fobj.write("This is a script to find and display files with its extension\n")
    fobj.write(Border+"\n")

    Ret=False
    Ret = os.path.exists(Directory)
    if(Ret == False):
        print("There is no such Directory")
        return
    
    Ret =os.path.isdir(Directory)
    if(Ret == False):
        print("Its not a Directory")
        return
    if not extension.startswith("."):
        extension="."+extension

    for Foldername,SubFolderName,Filename in os.walk(Directory):
        
        fobj.write(Border+"\n")
        fobj.write(f"File from {Foldername} scanning\n")
        fobj.write(f"Files with {extension} listed below\n")
        fobj.write(Border+"\n")

        for Fname in Filename:
            if(Fname.endswith(extension)):
                fobj.write(f"{Fname}\n")  
                   
        fobj.write(Border+"\n")
                      
    
    fobj.write("All files from "+(Directory)+" scanned successfully\n")
    fobj.write(Border+"\n")
    fobj.close()
    
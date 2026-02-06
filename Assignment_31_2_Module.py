import os
import time

timestamp=time.ctime()
Logfilename="Directory_File_Rename%s.log" %(timestamp)
Logfilename = Logfilename.replace(" ","_")
Logfilename=Logfilename.replace(":","_")
fobj=open(Logfilename,"w")
Border = "-"*80

    
def DirectoryFilesRename(Directory,ext1,ext2):
    
    fobj.write("This log file is created at "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("This is log file created by Marvellous Automation\n")
    fobj.write("This is a script to find and rename files to different extension\n")
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
    
    if not ext1.startswith("."):
        extension="."+ext1
    if not ext2.startswith("."):
        extension="."+ext2

    for Foldername,SubFolderName,Filename in os.walk(Directory):
        
        fobj.write(Border+"\n")
        fobj.write(f"File from {Foldername} scanning\n")
        fobj.write(f"Files with .{ext1} listed below\n")
        fobj.write(Border+"\n")

        for Fname in Filename:
            if(Fname.endswith(ext1)):
                File,extension = os.path.splitext(Fname)
                NewName =  File+ ext2

                old_path = os.path.join(Foldername, Fname)
                new_path = os.path.join(Foldername, NewName)
                fobj.write(f"File {old_path} with extension {ext1} rename with new extension {ext2} New Filename :{new_path}\n")
                
                os.rename(old_path, new_path)

        fobj.write(Border+"\n")
                      
    
    fobj.write("All files from "+(Directory)+" scanned successfully\n")
    fobj.write(Border+"\n")
    fobj.close()
    
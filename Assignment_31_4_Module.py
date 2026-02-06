import os
import time
import shutil
timestamp=time.ctime()
Logfilename="Directory_File_Copy%s.log" %(timestamp)
Logfilename = Logfilename.replace(" ","_")
Logfilename=Logfilename.replace(":","_")
fobj=open(Logfilename,"w")
Border = "-"*80

    
def DirectoryCopyExt(Directory1,Directory2,Extension):
    
    fobj.write("This log file is created at "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("This is log file created by Marvellous Automation\n")
    fobj.write("This is a script to Copy files to new directory with specified extension \n")
    fobj.write(Border+"\n")

    Ret=False
    Ret = os.path.exists(Directory1)
    if(Ret == False):
        print("There is no such Directory")
        return
    
    Ret =os.path.isdir(Directory1)
    if(Ret == False):
        print("Its not a Directory")
        return
    
    Ret = os.path.exists(Directory2)
    if(Ret == False):
        os.mkdir(Directory2)

    if not Extension.startswith("."):
        Extension="."+Extension
    for Foldername,SubFolderName,Filename in os.walk(Directory1):
        
        fobj.write(Border+"\n")
        fobj.write(f"File from {Foldername} scanning\n")
        fobj.write(f"Files from {Foldername} listed below\n")
        fobj.write(Border+"\n")

        for Fname in Filename:
            if Fname.endswith(Extension):
                src_path = os.path.join(Foldername, Fname)
                dest_path = os.path.join(Directory2, Fname)

                shutil.copy2(src_path, dest_path)
                fobj.write(f"Filename : {Fname} Extesnion:{Extension}\n")
        fobj.write(f"Files are loaded successfully into Directory :{Directory2}\n")       
        fobj.write(Border+"\n")
                      
    
    fobj.write("All files from "+(Directory1)+" scanned successfully\n")
    fobj.write(f"All files loaded into {Directory2}\n")
    fobj.write(Border+"\n")
    fobj.close()
    
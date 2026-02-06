import os
import hashlib
import time
def CalculateChecksum(Filename):
    fobj=open(Filename,"rb")
    try:
        hobj=hashlib.md5()

        Buffer=fobj.read(1000)

        while(len(Buffer)>0):
            hobj.update(Buffer)
            Buffer=fobj.read(1000)
        fobj.close()
        return hobj.hexdigest()
    except Exception as e:
        fobj.write(f"Error reading {Filename}: {e}")
        return None

def DirectoryScanning(Directory):
    Border = "-"*80
    timestamp=time.ctime()
    Logfilename="Assignment_32_1%s.log" %(timestamp)
    Logfilename = Logfilename.replace(" ","_")
    Logfilename=Logfilename.replace(":","_")
    fobj=open(Logfilename,"w")


    fobj.write("This log file is created at "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("This is log file created by Marvellous Automation\n")
    fobj.write("This is a script to calculate checksum of files\n")
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
    
    for Foldername,SubFolderName,Filename in os.walk(Directory):
        for Fname in Filename:
            Fname = os.path.join(Foldername,Fname)
            fobj.write("\n"+Fname+"File opened successfully\n")
            CheckSum=CalculateChecksum(Fname)
            fobj.write(f"Filename :{Fname} Checksum :{CheckSum}\n")
            
    fobj.write(Border+"\n")
    fobj.write("All files from "+(Directory)+"scaned successfully\n")
    fobj.write("Checksum of files calculated displayed successfully\n")
    fobj.write(Border+"\n")
    fobj.close()
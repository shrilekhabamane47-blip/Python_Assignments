import os
import hashlib
import time

timestamp=time.ctime()
Logfilename="Assignment_32_3_%s.log" %(timestamp)
Logfilename = Logfilename.replace(" ","_")
Logfilename=Logfilename.replace(":","_")
fobj=open(Logfilename,"w")
Border = "-"*80
def CalculateChecksum(Filename):
    fobj=open(Filename,"rb")
    try:
        hobj=hashlib.md5()

        Buffer=fobj.read(1024)

        while(len(Buffer)>0):
            hobj.update(Buffer)
            Buffer=fobj.read(1024)
        fobj.close()
        return hobj.hexdigest()
    except Exception as e:
        fobj.write(f"Error reading {Filename}: {e}")
        return None
    
def DirectoryScanning(Directory):
    
    fobj.write("This log file is created at "+timestamp+"\n")
    fobj.write(Border+"\n")
    fobj.write("This is log file created by Marvellous Automation\n")
    fobj.write("This is a script to find duplicate files from directory and delete it maintaing logs\n")
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
    Duplicate={}
    for Foldername,SubFolderName,Filename in os.walk(Directory):
        
        fobj.write(f"File from {Foldername}{SubFolderName} opened successfully\n")
        fobj.write(Border+"\n")
        fobj.write("Checksum of files from "+(Directory)+" is calculated\n")
        fobj.write(Border+"\n")
        for Fname in Filename:
            Fname = os.path.join(Foldername,Fname)
            
            CheckSum=CalculateChecksum(Fname)
            fobj.write(f"Filename : {Fname} Checksum :{CheckSum}\n")
            if(CheckSum in Duplicate):
                Duplicate[CheckSum].append(Fname)
            else:
                Duplicate[CheckSum] = [Fname]
        fobj.write(Border+"\n")
                      
    
    fobj.write("All files from "+(Directory)+" scanned successfully\n")
    
    fobj.write(Border+"\n")
    return Duplicate

def DeleteDuplicate(Directory):
    Duplicate_Dict = DirectoryScanning(Directory)

    Result=list(filter(lambda x:(len(x)>1), Duplicate_Dict.values()))
    
    if Result:
        fobj.write("\nDuplicate files found:\n")
        fobj.write(Border + "\n")
        for files in Result:
            for file in files:
                fobj.write(f"{file}\n")
            fobj.write(Border + "\n")

        for files in Result:
            for file in files[1:]:
                os.remove(file)
                fobj.write(f"{file} Deleted \n")
            fobj.write(Border + "\n")
    fobj.close()
    